import yaml


print(yaml.load(open("yamltest.yml"),Loader =yaml.FullLoader))
print(yaml.dump({'a': [1, 2]}))