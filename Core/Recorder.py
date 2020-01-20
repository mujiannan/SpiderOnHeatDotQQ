import json
import os
class Recorder:
    path_output=os.path.join(os.getcwd(),'OutPut')
    if not os.path.exists(path_output):
        os.makedirs(path_output)
    def save_json(self,obj_json,file_name,subpath=''):
        file_full_name=os.path.join(self.path_output,file_name)
        if os.path.exists(file_full_name):
            os.remove(file_full_name)
        file_output=open(file_full_name,'w',1)
        file_output.write(json.dumps(obj=obj_json))
        file_output.close()
