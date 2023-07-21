import importlib
import pkgutil


def register_blueprints(app, package, bp='bp'):
    spec = importlib.util.find_spec(package)
    mod = importlib.import_module(spec.name)

    for module_finder, name, ispkg in pkgutil.iter_modules(
            spec.submodule_search_locations, f'{package}.'):
        if ispkg:
            subspec = module_finder.find_spec(name)
            register_subblueprints(app, subspec, bp)


def register_subblueprints(blueprint, spec, bp='bp'):
    mod = importlib.import_module(spec.name)
    if not hasattr(mod, bp):
        return
    subblueprint = getattr(mod, bp)

    for module_finder, name, ispkg in pkgutil.iter_modules(
            spec.submodule_search_locations, f'{spec.name}.'):
        if ispkg:
            subspec = module_finder.find_spec(name)
            register_subblueprints(subblueprint, subspec, bp)

    blueprint.register_blueprint(subblueprint)
