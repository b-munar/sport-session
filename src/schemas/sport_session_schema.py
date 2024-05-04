from marshmallow import Schema, fields

class SportSessionDeserializeSchema(Schema):
    session = fields.String(required=True)

class SportSessionSerializeSchema(Schema):
    id = fields.UUID()
    session = fields.String()
    updateAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')
    createdAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')