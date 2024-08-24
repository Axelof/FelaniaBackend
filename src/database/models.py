from tortoise import Tortoise, fields, models


class BaseModel(models.Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True


class CreatedAtMixin:
    created_at = fields.DatetimeField(auto_now_add=True)


Tortoise.init_models(["database.models"], "models")
