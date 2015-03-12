yamlcfg
=======

Hierarchical YAML configuration utility for Python

yamlcfg makes it easier to have different levels of YAML configuration files,
with prioritization that you declare, based on the order of the `paths`
keyword argument.

It first checks your environment for the variable, and if it exists, it uses
that over anything else. Then it checks the first file in `paths`, or `path`,
and then the next in order until the variable is found. If not found, it returns
None.

Access is allowed via normal attribute access via the dot operator, or from
an index such as `config['myattr']`.

To dump the full configuration that was loaded back to file (first path in
`paths`), just invoke `write()`.

Example:

    from yamlcfg import YamlConfig
    config = YamlConfig(path='~/.some_config.yml')
    print(config.foo)
    config.foo = 'bar'
    config.write()

    fifo_configs = YamlConfig(paths=
      ('.myconfig.yml', '~/.userconfig.yml', '/etc/myconfig/defaultconfig.yml')
    )
    # First checks .myconfig.yml, and if it doesn't exist there, it checks
    # ~/.userconfig.yml, and so on. If an environment variable of the same name
    # is set, it will use that first.
    print(fifo_configs.some_var)
    # Dumps to the first path in paths, with every variable it found in order.
    fifo_configs.write()
