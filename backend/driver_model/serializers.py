from rest_framework import serializers

from driver_model import models


class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model    = models.DriverDetail
        fields   = ('id','full_name','gender','dob','contact','dob','address','martial_status',
            'vehicle_no','license_type','license_no','license_issue_office',
            'pan_no','citizenship_no','driving_license_file')
