class Config:
    #generate configuraion parent class
    pass

class ProdConfig(Config):
    #production configuration child
    pass

class DevConfig(Config):
    #development configuration child
    DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}