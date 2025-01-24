# MyFunctionApp/__init__.py
import datetime
import logging
import azure.functions as func
from ..optimize_resources import optimize_vm_resources

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    resource_group = "MyResourceGroup"
    vm_name = "MyVM"
    optimize_vm_resources(resource_group, vm_name)
    
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
