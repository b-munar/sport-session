from marshmallow import Schema, fields

class SportSessionDeserializeSchema(Schema):
    session = fields.String(required=True)

class SportSessionSerializeSchema(Schema):
    id = fields.UUID()
    trainingDay = fields.UUID()
    endDate = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')
    startDate = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')