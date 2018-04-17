import connexion
import six

from swagger_server.models.process import PROCESS  # noqa: E501
from swagger_server import util

from subprocess import Popen, PIPE
from re import split
from sys import stdout
import subprocess

 
def get_proc_list():
    ''' Retrieves a list [] of Proc objects representing the active
    process list list '''
    proc_list = []
    #command='docker run ritandon/swaggerprocess ps -aux'
    sub_proc = Popen(['ps', 'aux'], shell=False, stdout=PIPE)
    #sub_proc = Popen([command], shell=True, stdout=PIPE)
    #sub_proc = Popen("docker run ritandon/swaggerprocess ps -aux", stdin=PIPE) 
    #Discard the first line (ps aux header)
    sub_proc.stdout.readline()
    for line in sub_proc.stdout:
        #The separator for splitting is 'variable number of spaces'
        proc_info = split(" *", line.strip())
        #proc_list.append(Proc(proc_info))
	proc_list.append("User: " + proc_info[0] + " PID: " + proc_info[1] + " CPU%: "+ proc_info[2] + " MEM%: " + proc_info[3] + " START: " + proc_info[8] + " TIME: "+ proc_info[9] + " COMMAND: " + proc_info[10])
    return proc_list

def process_get():  # noqa: E501
    """process_get

    Returns process information of the hosting server # noqa: E501


    :rtype: PROCESS
    """
    #return 'do some magic!'
    return PROCESS(get_proc_list())


    
