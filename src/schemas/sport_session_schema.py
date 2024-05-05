from marshmallow import Schema, fields

class SportSessionDeserializeSchema(Schema):
    trainingDayId = fields.UUID()
    startDate = fields.String()
    endDate = fields.String()

class SportSessionSerializeSchema(Schema):
    id = fields.UUID()
    trainingDayId = fields.UUID()
    endDate = fields.String()
    startDate = fields.String()