# Publish Data from car device to Greengrass IoT
#
# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://aws.amazon.com/apache2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
#
#prueba 4.0 pipeline Sonar

import greengrasssdk
import json

# Greengrass client to publish to
client = greengrasssdk.client('iot-data')

# Executed on every messages received from the subscription (car1 and car 2 to Lambda)
def lambda_handler(event, context):
  
  # If the data comes from the cars
  if event['device'] in ['car1', 'car2']:
    # Publish to the lab/greengrass/telemetry what was received
    client.publish(topic='lab/greengrass/telemetry', payload=json.dumps(event))
  else:
    print "Not a valid Vehicle"
  return

