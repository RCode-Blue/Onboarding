from flask_restful import Resource, reqparse
from models.template import TemplateModel

class Template(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('template_id', type = int)
  parser.add_argument('template_name', type = str)
  parser.add_argument('description', type = str)
 
  
  # API Requests:
  # GET
  def get(self):
    data = Template.parser.parse_args()
    template = TemplateModel.find_by_id(data['template_id'])
    if template:
      return template.json_positions()
      # return template.json()
    
    return {"message": "Template not found"}, 404


  # PUT (edit)
  def put(self):
    data = Template.parser.parse_args()
    template = TemplateModel.find_by_template_name(data['template_name'])

    if template:
      template.template_name = data['template_name']
      template.description = data['description']

    else:
      newTemplate = TemplateModel(data['template_name'],
        data['description'])

      try:
        newTemplate.save_to_db()
        return newTemplate.json()
      except:
        return { "message": "An error occured inserting the Template" }, 500


  # POST (create new)
  def post(self):
    data = Template.parser.parse_args()
    if TemplateModel.find_by_template_name(data['template_name']):
      return {"message": "A template with that name already exists"}, 400

    data = Template.parser.parse_args()
    newTemplate = TemplateModel(
      data['template_name'],
      data['description']
    )

    try:
      newTemplate.save_to_db()
      return newTemplate.json(), 201
    except:
      return { "message": "An error occured inserting the template" }, 500

    

  # DELETE
  def delete(self):
    data = Template.parser.parse_args()
    template = TemplateModel.find_by_id(data['template_id'])

    if template:
      template.delete_from_db()
      return {"message": "Template deleted"}

    return {"message": "Template not found"}




class Templates(Resource):
  def get(self):
    return {"templates": [template.json() for template in TemplateModel.query.all()]}