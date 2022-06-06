import json
import os
import sys
import time
from datetime import date, datetime

import boto3
import pandas
from fr4nc3_ds_utils.api import responses

{%- if cookiecutter.install_clickhouse_driver|lower == 'yes' %}

{%- endif %}

{%- if cookiecutter.install_fr4nc3_ds_utils|lower == 'yes' %}

{%- endif %}


{%- if cookiecutter.install_pandas|lower == 'yes' %}

{%- endif %}


def lambda_handler(event, context):
    """rest_response
         This function is the main function for the filters lambda serverless 
     endpoint. It will recieve teh parameters 
    :param Object event:  
    :param Object contect:  serverless context
    :return:  response
    :rtype: Dict
    :raises: TypeError
    """
    body = {"name": "{{ cookiecutter.project_slug }}"}
    status_code: 200
    {%- if cookiecutter.install_fr4nc3_ds_utils|lower == 'yes' %}
    return responses.rest_response(status_code: status_code, body: body)
    {%- else %}
    return {
        "statusCode": status_code,
        "headers": {
            'Access-Control-Allow-Origin': '*'
        },
        "body": body
    }
    {%- endif %}
