from pydantic_settings import BaseSettings, SettingsConfigDict

# a sub library from pydantic used to validate config data like .env

# the nested classes below is a standard structure 
class Settings(BaseSettings):
    # here you define the same vars used in .env file in the chosen datatype
    model_config= SettingsConfigDict(

        # this to automatic check when every value changes
        validate_assignment=True,
        # the path to your file:
        env_file=".env",
        # to ignore validation to the non-mentioned vars below but mentioned in the .env
        extra="ignore"
        )
    APP_NAME: str
    APP_VERSION: str
    GEMINI_API_KEY: str
    FILE_ALLOWED_EXTENTIONS: list
    FILE_MAX_SIZE: int

def get_settings():
    return Settings()