from marshmallow import Schema, fields

class SportSessionDeserializeSchema(Schema):
    trainingDayId = fields.UUID()
    FTP = fields.Float()
    VO = fields.Float()
    RPM = fields.Float()
    KCAL = fields.Float()
    startDate = fields.String()
    endDate = fields.String()

class SportSessionSerializeSchema(Schema):
    id = fields.UUID()
    trainingDayId = fields.UUID()
    FTP = fields.Float()
    VO = fields.Float()
    RPM = fields.Float()
    KCAL = fields.Float()
    endDate = fields.String()
    startDate = fields.String()