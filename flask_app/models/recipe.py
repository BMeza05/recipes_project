# from flask import Flash
from flask.helpers import flash

from ..config.mysqlconnection import connectToMySQL

from ..models import user



class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.recipe_name = data['recipe_name']
        self.recipe_instructions = data['recipe_instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user']

    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO users_and_recipes.recipes (recipe_name, recipe_instructions, users_id, created_at, updated_at) VALUES ((%(recipe_name)s,%(recipe_instructions)s,%(users_id)s,NOW(),NOW());"

        return connectToMySQL("users_and_recipes").query_db(query, data)


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"

        results = connectToMySQL("users_and_recipes").query_db(query, data)

        if len(results) < 1:
            return False

        return cls(results[0])


    @classmethod
    def get_all(cls):
        query = "SELECT * from recipes;"

        results = connectToMySQL("users_and_recipes").query_db(query)

        recipes = []

        if len(results) > 0:
            for row in results:
                row_data = {
                    "id": row['id'],
                    "recipe_name": row['recipe_name'],
                    "recipe_instructions": row['recipe_instructions'],
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at'],
                    "user": user.User.get_by_id({"id": row ['user_id']})
                }
                recipes.append(cls(row_data))

        return recipes

    @classmethod
    def update(cls, data):
        pass


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s:"

        return connectToMySQL("users_and_recipes").query_db(query, data)



    @staticmethod
    def validate(post_data):
        is_valid = True

        if len(post_data['recipe_name']) < 3 :
            flash("Recipe name must be at least 3 characters")
            is_valid = False

        if len(post_data['recipe_instructions']) < 3 :
            flash("Recipe instructions must be at least 3 characters")
            is_valid = False

        return is_valid