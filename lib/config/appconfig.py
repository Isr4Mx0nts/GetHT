import yaml


class ApplicationConfig:	
	def __init__(self, filename, section=None):
		yaml_config = yaml.load(file(filename))
		if section is not None:
			config_section = yaml_config.get(section, None)
		else:
			config_section = yaml_config

		self.config = config_section

	def get_property(self, property_name):
		return self.config.get(property_name, None)


class TwitterConfig(ApplicationConfig):
	def __init__(self,  filename, section='twitter'):
		ApplicationConfig.__init__(self, filename, section)
class CorreoConfig(ApplicationConfig):
	def __init__(self, filename, section='correo'):
		ApplicationConfig.__init__(self, filename, section)
