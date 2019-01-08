from flask_restful import Resource, reqparse
from models.template import TemplateModel

class TemplateResource(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('sequence_id',
    type = str)
  parser.add_argument('description',
    type = str)
  parser.add_argument('city',
    type = str)
  parser.add_argument('start_date',
    type = str)
  parser.add_argument('employee_id',
    type = str)
  parser.add_argument('manager_id',
    type = str)
  parser.add_argument('buddy_id',
    type = str)

  
  # API Requests:
  # GET
  def get(self, templateid):
    template = TemplateModel.find_by_id(templateid)
    if template:
      return template.json_sequence()
    return {'message:' 'Template not found'}, 404

  # POST


  # DELETE



  # PUT