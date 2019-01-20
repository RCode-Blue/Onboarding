from flask_restful import Resource, reqparse
from models.template import TemplateModel

class Template(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('template_name',
    type = str)
  parser.add_argument('description',
    type = str)
 
  
  # API Requests:
  # GET
  def get(self, templateid):
    template = TemplateModel.find_by_id(templateid)
    if template:
      return template.json_positions()
    return {'message:' 'Template not found'}, 404

  # POST
  def post(self, templateid):
    if TemplateModel.find_by_id(templateid):
      return {"message": "A template with that id already exists"}, 400

    data = Template.parser.parse_args()
    print(data)
    template = TemplateModel(
      data['template_name'],
      data['description']
    )

    try:
      template.save_to_db()
    except:
      return { "message": "An error occured inserting the Template" }, 500

    return template.json(), 201

  # DELETE



  # PUT



class Templates(Resource):
  def get(self):
    return {"templates": [template.json() for template in TemplateModel.query.all()]}