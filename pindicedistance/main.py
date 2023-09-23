from app import App

app = App.load_config("./config.json")

app.run()