from __future__ import print_function

import urllib
import boto3
import openpyxl as px
import uuid

class HabitatBuild:
    start_time = " 7:00 AM"
    end_time = " 4:00 PM"
    def __init__(self, donor, volunteer_group, special_event, family_name, address, lot, community, day, build_day_number):
        self.donor = donor
        self.volunteer_group = volunteer_group
        self.special_event = special_event
        self.family_name = family_name
        self.address = address
        self.lot = lot
        self.community = community
        self.day = day
        self.build_day_number = build_day_number
    def get_location(self):
        return "{} - lot {}".format(self.community, self.lot)
    def get_description(self):
        if self.special_event and self.special_event != "":
            return "Event: {}\nFor: {}\nSponsored by: {}\nVolunteer Group: {}".format(self.special_event, self.family_name, self.donor, self.volunteer_group)
        else:
            return "For: {}\nSponsored By: {}\nVolunteer Group: {}".format(self.family_name, self.donor, self.volunteer_group)
    def get_name(self):
        return "{} - Build Day #{}".format(self.get_location(), self.build_day_number)
    def __str__(self):
        return "name: {}\nlocation: {}\naddress: {}\ndate:{}\ndescription: {}\n"\
            .format(self.get_name(), self.get_location(), self.address, str(self.day), self.get_description())



def read_xls_into_habitat_builds(input_file):
    W = px.load_workbook(input_file, use_iterators = True)
    p = W.get_sheet_by_name(name = 'Sheet1')
    builds = []
    first = True
    for row in p.iter_rows():
        if first:
            first = False
            continue
        build_day_number = 1
        for day in row[11:19]:
            if day.value:
                build = HabitatBuild(
                    row[1].value, row[3].value, row[4].value, row[6].value, row[7].value, row[8].value, row[9].value, day.value, build_day_number)
                builds.append(build)
            build_day_number = 1 + build_day_number
    return builds

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    # Get the xlsx file from the 'event' and parse the builds from it
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')
    try:
        s3_obj = s3.get_object(Bucket=bucket, Key=key)
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        print("Downloading to " + download_path)
        s3.download_file(bucket, key, download_path)

        print("Parsing XLSX file at "+ download_path)
        builds = read_xls_into_habitat_builds(download_path)

        for build in builds:
            print(build)
        #body = s3_obj['Body']

        return "Parsed out {} builds".format(len(builds))
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e