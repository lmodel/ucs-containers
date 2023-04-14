export type OpenContainerInitiativeId = string
export type LinuxContainersProjectId = string
export type ContainerId = string
export type LxcId = string
export type LxcFsId = string
export type LxdId = string
export type OciContainerId = string
export type PodmanId = string
export type ContainerdId = string
export type DockerId = string
export type KubernetesId = string
export type EntityId = string
export type NamedThingId = string
export type AdministrativeEntityId = string
export type AgentId = string
export type InformationContentEntityId = string
export type PublicationId = string
export type EvidenceTypeId = string
export type ProjectId = string
export type SystemId = string
export type SoftwareOrDeviceId = string
export type SoftwareId = string
export type HardwareId = string
export type OperatingSystemId = string
export type SolarisId = string
export type LinuxId = string
export type WindowsId = string
export type AssociationId = string
/**
 * An open governance structure for express purpose of creating open industry standards around container formats and runtime.
 */
export interface OpenContainerInitiative  extends Project, OpenSource  {
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Linux Containers is umbrella project for LXD, LXC, LXCFS and distrobuilder.
 */
export interface LinuxContainersProject  extends Project, OpenSource  {
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Software that emulates a whole computer by means of an isolated user-space environment running on top of the operating system's kernel.
 */
export interface Container  extends Software, Virtualization  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Operating system-level virtualization for Linux
 */
export interface Lxc  extends Software, Virtualization, LinuxContainersProject  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * LXCFS is a simple userspace filesystem designed to work around some current limitations of the Linux kernel.
 */
export interface LxcFs  extends Software, LinuxContainersProject  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Lxd is a system container and virtual machine manager for Linux OS
 */
export interface Lxd  extends Software, LinuxContainersProject  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Open Container Initiative (OCI) compliant containers
 */
export interface OciContainer  extends Container, OpenContainerInitiative  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * daemonless OCI-compliant container runtime
 */
export interface Podman  extends Software, OpenContainerInitiative  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Container runtime
 */
export interface Containerd  extends Software, OpenContainerInitiative  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * open-source software for deploying containerized applications
 */
export interface Docker  extends Software  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * software to manage containers on a server-cluster
 */
export interface Kubernetes  extends Software  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Self contained software module
 */
export interface ClosedSoftwareModule  {
    /**
     * file that can be directly run by a computer
     */executable?: string,
}
/**
 * Podman container
 */
export interface PodmanContainer  extends ClosedSoftwareModule  {
    /**
     * absent - A container matching the specified name will be stopped and removed.
present - Asserts the existence of a container matching the name and any provided configuration parameters. If no container matches the name, a container will be created. If a container matches the name but the provided configuration does not match, the container will be updated, if it can be. If it cannot be updated, it will be removed and re-created with the requested config. Image version will be taken into account when comparing configuration. Use the recreate option to force the re-creation of the matching container.
started - Asserts there is a running container matching the name and any provided configuration. If no container matches the name, a container will be created and started. Use recreate to always re-create a matching container, even if it is running. Use force_restart to force a matching container to be stopped and restarted.
stopped - Asserts that the container is first present, and then if the container is running moves it to a stopped state.
created - Asserts that the container exists with given configuration. If container doesn’t exist, the module creates it and leaves it in ‘created’ state. If configuration doesn’t match or ‘recreate’ option is set, the container will be recreated
     */state?: string,
    /**
     * Add an annotation to the container. The format is key value, multiple times.
     */annotation?: MetaObject,
    /**
     * Path of the authentication file. Default is ``${XDG_RUNTIME_DIR}/containers/auth.json`` (Not available for remote commands) You can also override the default path of the authentication file by setting the ``REGISTRY_AUTH_FILE`` environment variable. ``export REGISTRY_AUTH_FILE=path``
     */authfile?: string,
    /**
     * Block IO weight (relative weight) accepts a weight value between 10 and 1000        minimum_value: 10
     */blkio_weight?: number,
    /**
     * Block IO weight (relative device weight, format DEVICE_NAME[:]WEIGHT).
     */blkio_weight_device?: MetaObject[],
    /**
     * List of capabilities to add to the container.
     */cap_add?: string,
    /**
     * List of capabilities to drop from the container.
     */cap_drop?: string,
    /**
     * Path to cgroups under which the cgroup for the container will be created. If the path is not absolute, the path is considered to be relative to the cgroups path of the init process. Cgroups will be created if they do not already exist.
     */cgroup_parent?: string,
    /**
     * Path to cgroups under which the cgroup for the container will be created.
     */cgroupns?: string,
    /**
     * Determines whether the container will create CGroups. Valid values are enabled and disabled, which the default being enabled. The disabled option will force the container to not create CGroups, and thus conflicts with CGroup options cgroupns and cgroup-parent.
     */cgroups?: string,
    /**
     * Write the container ID to the file
     */cidfile?: string,
    /**
     * Any additional command options you want to pass to podman command, cmd_args - [’–other-param’, ‘value’] Be aware module doesn’t support idempotency if this is set.
     */cmd_args?: string,
    /**
     * Write the pid of the conmon process to a file. conmon runs in a separate process than Podman, so this is necessary when using systemd to restart Podman containers.
     */conmon_pidfile?: string,
    /**
     * Override command of container. Can be a string or a list.
     */command?: string,
    /**
     * Limit the CPU real-time period in microseconds
     */cpu_period?: number,
    /**
     * Limit the CPU real-time period in microseconds. Limit the container’s Real Time CPU usage. This flag tell the kernel to restrict the container’s Real Time CPU usage to the period you specify.
     */cpu_rt_period?: number,
    /**
     * Limit the CPU real-time runtime in microseconds. This flag tells the kernel to limit the amount of time in a given CPU period Real Time tasks may consume.
     */cpu_rt_runtime?: number,
    /**
     * CPU shares (relative weight)
     */cpu_shares?: number,
    /**
     * Number of CPUs. The default is 0.0 which means no limit.
     */cpus?: string,
    /**
     * CPUs in which to allow execution (0-3, 0,1)
     */cpuset_cpus?: string,
    /**
     * Memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems.
     */cpuset_mems?: string,
    /**
     * Run container in detach mode
     */detach?: boolean,
    /**
     * Return additional information which can be helpful for investigations.
     */debug?: boolean,
    /**
     * Override the key sequence for detaching a container. Format is a single character or ctrl-value
     */detach_keys?: string,
    /**
     * Add a host device to the container. The format is <device-on-host>[:<device-on-container>][:<permissions>] (e.g. device /dev/sdc:/dev/xvdc:rwm)
     */device?: string,
    /**
     * Limit read rate (bytes per second) from a device (e.g. device-read-bps /dev/sda:1mb)
     */device_read_bps?: string,
    /**
     * Limit read rate (IO per second) from a device (e.g. device-read-iops /dev/sda:1000)
     */device_read_iops?: string,
    /**
     * Limit write rate (bytes per second) to a device (e.g. device-write-bps /dev/sda:1mb)
     */device_write_bps?: string,
    /**
     * Limit write rate (IO per second) to a device (e.g. device-write-iops /dev/sda:1000)
     */device_write_iops?: string,
    /**
     * Set custom DNS servers
     */dns?: string,
    /**
     * Set custom DNS options
     */dns_option?: string,
    /**
     * Set custom DNS search domains (Use dns_search with ‘’ if you don’t wish to set the search domain)
     */dns_search?: string,
    /**
     * Overwrite the default ENTRYPOINT of the image
     */entrypoint?: string,
    /**
     * Set environment variables. This option allows you to specify arbitrary environment variables that are available for the process that will be launched inside of the container.
     */env?: MetaObject,
    /**
     * Read in a line delimited file of environment variables. Doesn’t support idempotency. If users changes the file with environment variables it’s on them to recreate the container.
     */env_file?: string,
    /**
     * Use all current host environment variables in container. Defaults to false.
     */env_host?: boolean,
    /**
     * Dict of host-to-IP mappings, where each host name is a key in the dictionary. Each host name will be added to the container’s ``/etc/hosts`` file.
     */etc_hosts?: MetaObject,
    /**
     * Expose a port, or a range of ports (e.g. expose “3300-3310”) to set up port redirection on the host system.
     */expose?: string,
    /**
     * Force restart of container.
     */force_restart?: boolean,
    /**
     * Generate systemd unit file for container.
     */generate_systemd?: MetaObject,
    /**
     * Run the container in a new user namespace using the supplied mapping.
     */gidmap?: string,
    /**
     * Add additional groups to run as
     */group_add?: string,
    /**
     * Set or alter a healthcheck command for a container.
     */healthcheck?: string,
    /**
     * Set an interval for the healthchecks (a value of disable results in no automatic timer setup) (default “30s”)
     */healthcheck_interval?: string,
    /**
     * The number of retries allowed before a healthcheck is considered to be unhealthy. The default value is 3.
     */healthcheck_retries?: number,
    /**
     * The initialization time needed for a container to bootstrap. The value can be expressed in time format like 2m3s. The default value is 0s
     */healthcheck_start_period?: string,
    /**
     * The maximum time allowed to complete the healthcheck before an interval is considered failed. Like start-period, the value can be expressed in a time format such as 1m22s. The default value is 30s
     */healthcheck_timeout?: string,
    /**
     * Container host name. Sets the container host name that is available inside the container.
     */hostname?: string,
    /**
     * By default proxy environment variables are passed into the container if set for the podman process. This can be disabled by setting the http_proxy option to false. The environment variables passed in include http_proxy, https_proxy, ftp_proxy, no_proxy, and also the upper case versions of those. Defaults to true
     */http_proxy?: boolean,
    /**
     * Tells podman how to handle the builtin image volumes. The options are bind, tmpfs, or ignore (default bind)
     */image_volume?: string,
    /**
     * Whether to compare images in idempotency by taking into account a full name with registry and namespaces.
     */image_strict?: boolean,
    /**
     * Run an init inside the container that forwards signals and reaps processes. The default is false.
     */init?: boolean,
    /**
     * Path to the container-init binary.
     */init_path?: string,
    /**
     * Keep STDIN open even if not attached. The default is false. When set to true, keep stdin open even if not attached. The default is false.
     */interactive?: boolean,
    /**
     * Specify a static IP address for the container, for example ‘10.88.64.128’. Can only be used if no additional CNI networks to join were specified via ‘network:’, and if the container is not joining another container’s network namespace via ‘network container:<name|id>’. The address must be within the default CNI network’s pool (default 10.88.0.0/16).
     */ip?: string,
    /**
     * Default is to create a private IPC namespace (POSIX SysV IPC) for the container
     */ipc?: string,
    /**
     * Kernel memory limit (format <number>[<unit>], where unit = b, k, m or g) Note - idempotency is supported for integers only.
     */kernel_memory?: string,
    /**
     * Add metadata to a container, pass dictionary of label names and values
     */label?: MetaObject,
    /**
     * Read in a line delimited file of labels
     */label_file?: string,
    /**
     * Logging driver. Used to set the log driver for the container. For example log_driver “k8s-file”.
     */log_driver?: string,
    /**
     * Logging level for Podman. Log messages above specified level (“debug”|”info”|”warn”|”error”|”fatal”|”panic”) (default “error”)
     */log_level?: string,
    /**
     * Logging driver specific options. Used to set the path to the container log file.
     */log_opt?: MetaObject,
    /**
     * Specify a MAC address for the container, for example ‘92:d0:c6:0a:29:33’. Don’t forget that it must be unique within one Ethernet network.
     */mac_address?: string,
    /**
     * Memory limit (format 10k, where unit = b, k, m or g) Note - idempotency is supported for integers only.
     */memory?: string,
    /**
     * Memory soft limit (format 100m, where unit = b, k, m or g) Note - idempotency is supported for integers only.
     */memory_reservation?: string,
    /**
     * A limit value equal to memory plus swap. Must be used with the -m (–memory) flag. The swap LIMIT should always be larger than -m (–memory) value. By default, the swap LIMIT will be set to double the value of –memory Note - idempotency is supported for integers only.
     */memory_swap?: string,
    /**
     * Tune a container’s memory swappiness behavior. Accepts an integer between 0 and 100.
     */memory_swappiness?: number,
    /**
     * Attach a filesystem mount to the container. bind or tmpfs For example mount “type=bind,source=/path/on/host,destination=/path/in/container”
     */mount?: string,
    /**
     * Name of the container
     */name?: string,
    /**
     * Set the Network mode for the container * bridge create a network stack on the default bridge * none no networking * container:<name|id> reuse another container’s network stack * host use the podman host network stack. * <network-name>|<network-id> connect to a user-defined network * ns:<path> path to a network namespace to join * slirp4netns use slirp4netns to create a user network stack. This is the default for rootless containers
     */network?: string,
    /**
     * Add network-scoped alias for the container. A container will only have access to aliases on the first network that it joins. This is a limitation that will be removed in a later release.
     */network_aliases?: string,
    /**
     * Do not create /etc/hosts for the container Default is false.
     */no_hosts?: boolean,
    /**
     * Whether to disable OOM Killer for the container or not. Default is false.
     */oom_kill_disable?: boolean,
    /**
     * Tune the host’s OOM preferences for containers (accepts -1000 to 1000)
     */oom_score_adj?: number,
    /**
     * Set the PID mode for the container
     */pid?: string,
    /**
     * Tune the container’s PIDs limit. Set -1 to have unlimited PIDs for the container.
     */pids_limit?: number,
    /**
     * Run container in an existing pod. If you want podman to make the pod for you, prefix the pod name with “new:”
     */pod?: string,
    /**
     * Give extended privileges to this container. The default is false.
     */privileged?: boolean,
    /**
     * Publish a container’s port, or range of ports, to the host. Format - ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort | containerPort In case of only containerPort is set, the hostPort will chosen randomly by Podman.
     */publish?: string,
    /**
     * Publish all exposed ports to random ports on the host interfaces. The default is false.
     */publish_all?: boolean,
    /**
     * Mount the container’s root filesystem as read only. Default is false
     */read_only?: boolean,
    /**
     * If container is running in –read-only mode, then mount a read-write tmpfs on /run, /tmp, and /var/tmp. The default is true
     */read_only_tmpfs?: boolean,
    /**
     * Use with present and started states to force the re-creation of an existing container.
     */recreate?: boolean,
    /**
     * Specify one or more requirements. A requirement is a dependency container that will be started before this container. Containers can be specified by name or ID.
     */requires?: string,
    /**
     * Restart policy to follow when containers exit. Restart policy will not take effect if a container is stopped via the podman kill or podman stop commands. Valid values are * no - Do not restart containers on exit * on-failure[:max_retries] - Restart containers when they exit with a non-0 exit code, retrying indefinitely or until the optional max_retries count is hit * always - Restart containers when they exit, regardless of status, retrying indefinitely
     */restart_policy?: string,
    /**
     * Automatically remove the container when it exits. The default is false.
     */rm?: boolean,
    /**
     * If true, the first argument refers to an exploded container on the file system. The default is false.
     */rootfs?: boolean,
    /**
     * Determines how to use the NOTIFY_SOCKET, as passed with systemd and Type=notify. Can be container, conmon, ignore.
     */sdnotify?: string,
    /**
     * Add the named secrets into the container. The format is secret[,opt=opt...], see documentation for more details.
     */secrets?: string,
    /**
     * Security Options. For example security_opt “seccomp=unconfined”
     */security_opt?: string,
    /**
     * Size of /dev/shm. The format is <number><unit>. number must be greater than 0. Unit is optional and can be b (bytes), k (kilobytes), m(megabytes), or g (gigabytes). If you omit the unit, the system uses bytes. If you omit the size entirely, the system uses 64m
     */shm_size?: string,
    /**
     * Proxy signals sent to the podman run command to the container process. SIGCHLD, SIGSTOP, and SIGKILL are not proxied. The default is true.
     */sig_proxy?: boolean,
    /**
     * Signal to stop a container. Default is SIGTERM.
     */stop_signal?: number,
    /**
     * Timeout (in seconds) to stop a container. Default is 10.
     */stop_timeout?: number,
    /**
     * Run the container in a new user namespace using the map with ‘name’ in the /etc/subgid file.
     */subgidname?: string,
    /**
     * Run the container in a new user namespace using the map with ‘name’ in the /etc/subuid file.
     */subuidname?: string,
    /**
     * Configure namespaced kernel parameters at runtime
     */sysctl?: MetaObject,
    /**
     * Run container in systemd mode. The default is true.
     */systemd?: string,
    /**
     * Set timezone in container. This flag takes area-based timezones, GMT time, as well as local, which sets the timezone in the container to match the host machine. See /usr/share/zoneinfo/ for valid timezones. Remote connections use local containers.conf for defaults.
     */timezone?: string,
    /**
     * Create a tmpfs mount. For example tmpfs “/tmp” “rw,size=787448k,mode=1777”
     */tmpfs?: MetaObject,
    /**
     * Allocate a pseudo-TTY. The default is false.
     */tty?: boolean,
    /**
     * Run the container in a new user namespace using the supplied mapping.
     */uidmap?: string,
    /**
     * Ulimit options
     */ulimit?: string,
    /**
     * Sets the username or UID used and optionally the groupname or GID for the specified command.
     */user?: string,
    /**
     * Set the user namespace mode for the container. It defaults to the PODMAN_USERNS environment variable. An empty value means user namespaces are disabled.
     */userns?: string,
    /**
     * Set the UTS mode for the container
     */uts?: string,
    /**
     * Create a bind mount. If you specify, volume /HOST-DIR:/CONTAINER-DIR, podman bind mounts /HOST-DIR in the host to /CONTAINER-DIR in the podman container.
     */volume?: string,
    /**
     * Mount volumes from the specified container(s).
     */volumes_from?: string,
    /**
     * Working directory inside the container. The default working directory for running binaries within a container is the root directory (/).
     */workdir?: string,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * Podman containers
 */
export interface PodmanContainers  extends ClosedSoftwareModule  {
    /**
     * List of dictionaries with data for running containers for podman_container module.
     */containers?: MetaObject[],
    /**
     * Return additional information which can be helpful for investigations.
     */debug?: boolean,
    /**
     * file that can be directly run by a computer
     */executable?: string,
}
/**
 * Export a Podman container
 */
export interface PodmanExport  extends ClosedSoftwareModule  {
    /**
     * Container to export.
     */container?: string,
    /**
     * Path to export container to.
     */dest?: string,
    /**
     * Force saving to file even if it exists.
     */force?: boolean,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * Generate systemd unit from a pod or a container
 */
export interface PodmanGenerateSystemd  extends ClosedSoftwareModule  {
    /**
     * Add the systemd unit after (After=) option, that ordering dependencies between the list of dependencies and this service.  This option may be specified more than once.  User-defined dependencies will be appended to the generated unit file. But any existing options such as needed or defined by default (e.g. online.target) will not be removed or overridden.  Only with Podman 4.0.0 and above
     */after?: string,
    /**
     * Set the systemd unit name prefix for containers. If not set, use the default defined by podman, container. Refer to podman-generate-systemd(1) man page for more information.
     */container_prefix?: string,
    /**
     * Destination of the generated systemd unit file(s)
     */dest?: string,
    /**
     * Set environment variables to the systemd unit files. Keys are the environment variable names, and values are the environment variable values. Only with Podman 4.3.0 and above
     */env?: MetaObject,
    /**
     * Name of the pod or container to export
     */name?: string,
    /**
     * Generate unit files that create containers and pods, not only start them. Refer to podman-generate-systemd(1) man page for more information.
     */new?: boolean,
    /**
     * Do not generate the header including meta data such as the Podman version and the timestamp.
     */no_header?: boolean,
    /**
     * Set the systemd unit name prefix for pods. If not set, use the default defined by podman, pod. Refer to podman-generate-systemd(1) man page for more information.
     */pod_prefix?: string,
    /**
     * Set the systemd unit requires (Requires=) option. Similar to wants, but declares a stronger requirement dependency. Only with Podman 4.0.0 and above
     */requires?: string,
    /**
     * Restart policy of the service
     */restart_policy?: string,
    /**
     * Configures the time to sleep before restarting a service (as configured with restart-policy).  Takes a value in seconds. Only with Podman 4.0.0 and above
     */restart_sec?: number,
    /**
     * Systemd unit name separator between the name/id of a container/pod and the prefix. If not set, use the default defined by podman, -. Refer to podman-generate-systemd(1) man page for more information.
     */separator?: string,
    /**
     * Override the default start timeout for the container with the given value in seconds. Only with Podman 4.0.0 and above
     */start_timeout?: number,
    /**
     * Override the default stop timeout for the container with the given value in seconds.
     */stop_timeout?: number,
    /**
     * Use name of the containers for the start, stop, and description in the unit file.
     */use_names?: boolean,
    /**
     * Wanted things
     */wants?: string,
    /**
     * Podman executable name or full path
     */executable?: string,
}
/**
 * Podman container image
 */
export interface PodmanImage  extends ClosedSoftwareModule  {
    /**
     * Path to file containing authorization credentials to the remote registry.
     */auth_file?: string,
    /**
     * Arguments that control image build.
     */build?: MetaObject,
    /**
     * Path to directory containing TLS certificates and keys to use.
     */ca_cert_dir?: string,
    /**
     * Whether or not to force push or pull an image. When building, force the build even if the image already exists.
     */force?: boolean,
    /**
     * Name of the image to pull, push, or delete. It may contain a tag using the format image:tag.
     */name?: string,
    /**
     * Password to use when authenticating to remote registries.
     */password?: string,
    /**
     * Path to the build context directory.
     */path?: string,
    /**
     * Whether or not to pull the image.
     */pull?: boolean,
    /**
     * Whether or not to push an image.
     */push?: boolean,
    /**
     * Arguments that control pushing images.
     */push_args?: MetaObject,
    /**
     * Process of encoding information using fewer bits than original representation
     */compress?: string,
    /**
     * Location where item appears, appeared, or is intended to be after transition
     */dest?: string,
    format?: string,
    /**
     * Discard any pre-existing signatures
     */remove_signatures?: string,
    /**
     * Path to a key file to use to sign the package.
     */sign_by?: string,
    /**
     * Human-directed movement of things or people between locations
     */transport?: string,
    /**
     * Whether an image should be present, absent, or built.
     */state?: string,
    /**
     * Tag of the image to pull, push, or delete.
     */tag?: string,
    /**
     * username to use when authenticating to remote registries.
     */username?: string,
    /**
     * Require HTTPS and validate certificates when pulling or pushing. Also used during build if a pull or push is necessary.
     */validate_certs?: boolean,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman.
     */executable?: string,
}
/**
 * Import Podman container from file
 */
export interface PodmanImport  extends ClosedSoftwareModule  {
    /**
     * Set changes as list of key-value pairs, see example.
     */change?: MetaObject[],
    /**
     * Set commit message for imported image
     */commit_message?: string,
    /**
     * Path to image file to load.
     */src?: string,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * Load container into container storage
 */
export interface PodmanLoad  extends ClosedSoftwareModule  {
    /**
     * Path to image file to load.
     */input?: string,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * Login to a Container registry using Podman
 */
export interface PodmanLogin  extends ClosedSoftwareModule  {
    /**
     * Path of the authentication file. Default is ``${XDG_RUNTIME_DIR}/containers/auth.json`` You can also override the default path of the authentication file by setting the ``REGISTRY_AUTH_FILE`` environment variable. ``export REGISTRY_AUTH_FILE=path``
     */authfile?: string,
    /**
     * Use certificates at path (*.crt, *.cert, *.key) to connect to the registry. Default certificates directory is /etc/containers/certs.d.
     */certdir?: string,
    /**
     * Password for the registry server.
     */password?: string,
    /**
     * Registry server. If the registry is not specified, the first registry under `[registries.search]` from `registries.conf` will be used.
     */registry?: string,
    /**
     * Require HTTPS and verify certificates when contacting registries. If explicitly set to true, then TLS verification will be used. If set to false, then TLS verification will not be used. If not specified, TLS verification will be used unless the target registry is listed as an insecure registry in registries.conf.
     */tlsverify?: boolean,
    /**
     * Username for the registry server.
     */username?: string,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * Logout of a Container registry using Podman
 */
export interface PodmanLogout  extends ClosedSoftwareModule  {
    /**
     * Remove the cached credentials for all registries in the auth file.
     */all?: boolean,
    /**
     * Path of the authentication file. Default is ``${XDG_RUNTIME_DIR}/containers/auth.json`` You can also override the default path of the authentication file by setting the ``REGISTRY_AUTH_FILE`` environment variable. ``export REGISTRY_AUTH_FILE=path``
     */authfile?: string,
    /**
     * Credentials created using other tools such as `docker login` are not removed unless the corresponding `authfile` is explicitly specified. Since podman also uses existing credentials in these files by default (for docker e.g. `${HOME}/.docker/config.json`), module execution will fail if a docker login exists for the registry specified in any `authfile` is used by podman. This can be ignored by setting `ignore_docker_credentials` to `yes` - the credentials will be kept and `changed` will be false. This option cannot be used together with `all` since in this case podman will not check for existing `authfiles` created by other tools.
     */ignore_docker_credentials?: boolean,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * Manage podman networks
 */
export interface PodmanNetwork  extends ClosedSoftwareModule  {
    /**
     * Return additional information which can be helpful for investigations.
     */debug?: boolean,
    /**
     * disable dns plugin (default “false”)
     */disable_dns?: boolean,
    /**
     * Driver to manage the network (default “bridge”)
     */driver?: string,
    /**
     * IPv4 or IPv6 gateway for the subnet
     */gateway?: string,
    /**
     * Restrict external access from this network (default “false”)
     */internal?: boolean,
    /**
     * Allocate container IP from range
     */ip_range?: string,
    /**
     * Enable IPv6 (Dual Stack) networking. You must pass a IPv6 subnet. The subnet option must be used with the ipv6 option.
     */ipv6?: boolean,
    /**
     * Create a Macvlan connection based on this device
     */macvlan?: string,
    /**
     * Name of the network
     */name?: string,
    /**
     * Add network options. Currently ‘vlan’ and ‘mtu’ are supported.
     */opt?: MetaObject,
    /**
     * Recreate network even if exists.
     */recreate?: boolean,
    /**
     * State of network, default ‘present’
     */state?: string,
    /**
     * Subnet in CIDR format
     */subnet?: string,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman ifabsent: string(podman)
     */executable?: string,
}
/**
 * Play kubernetes YAML file using podman
 */
export interface PodmanPlay  extends ClosedSoftwareModule  {
    /**
     * Path of the authentication file. Default is ${XDG_RUNTIME_DIR}/containers/auth.json, which is set using podman login. If the authorization state is not found there, $HOME/.docker/config.json is checked, which is set using docker login. Note - You can also override the default path of the authentication file by setting the REGISTRY_AUTH_FILE environment variable. export REGISTRY_AUTH_FILE=path
     */authfile?: string,
    /**
     * Use certificates at path (*.crt, *.cert, *.key) to connect to the registry. Default certificates directory is /etc/containers/certs.d. (This option is not available with the remote Podman client)
     */cert_dir?: string,
    /**
     * Use Kubernetes configmap YAML at path to provide a source for environment variable values within the containers of the pod. Note - The configmap option can be used multiple times to pass multiple Kubernetes configmap YAMLs
     */configmap?: string,
    /**
     * Enable debug for the module.
     */debug?: boolean,
    /**
     * Path to file with YAML configuration for a Pod.
     */kube_file?: string,
    /**
     * Set logging driver for all created containers.
     */log_driver?: string,
    /**
     * Set logging level for podman calls. Log messages above specified level (“debug”|”info”|”warn”|”error”|”fatal”|”panic”) (default “error”)
     */log_level?: string,
    /**
     * List of the names of CNI networks the pod should join.
     */network?: string,
    /**
     * The username and password to use to authenticate with the registry if required.
     */password?: string,
    /**
     * Hide image pulls logs from output.
     */quiet?: boolean,
    /**
     * If pod already exists, delete it and run the new one.
     */recreate?: boolean,
    /**
     * Directory path for seccomp profiles (default is “/var/lib/kubelet/seccomp”). This option is not available with the remote Podman client
     */seccomp_profile_root?: string,
    /**
     * Start the pod after creating it, or to leave it created only.
     */state?: string,
    /**
     * Require HTTPS and verify certificates when contacting registries (default is true). If explicitly set to true, then TLS verification will be used. If set to false, then TLS verification will not be used. If not specified, TLS verification will be used unless the target registry is listed as an insecure registry in registries.conf.
     */tls_verify?: boolean,
    /**
     * The username and password to use to authenticate with the registry if required.
     */username?: string,
    /**
     * Name of executable to run, by default ‘podman’ ifabsent: string(podman)
     */executable?: string,
}
/**
 * Manage Podman pods
 */
export interface PodmanPod  extends ClosedSoftwareModule  {
    /**
     * Add a host to the /etc/hosts file shared between all containers in the pod.
     */add_host?: string,
    /**
     * Path to cgroups under which the cgroup for the pod will be created. If the path is not absolute, he path is considered to be relative to the cgroups path of the init process. Cgroups will be created if they do not already exist.
     */cgroup_parent?: string,
    /**
     * Set the total number of CPUs delegated to the pod. Default is 0.000 which indicates that there is no limit on computation power.
     */cpus?: string,
    /**
     * Limit the CPUs to support execution. First CPU is numbered 0. Unlike `cpus` this is of type string and parsed as a list of numbers. Format is 0-3,0,1
     */cpuset_cpus?: string,
    /**
     * Return additional information which can be helpful for investigations.
     */debug?: boolean,
    /**
     * Add a host device to the pod. Optional permissions parameter can be used to specify device permissions. It is a combination of r for read, w for write, and m for mknod(2)
     */device?: string,
    /**
     * Limit read rate (bytes per second) from a device (e.g. device-read-bps=/dev/sda:1mb)
     */device_read_bps?: string,
    /**
     * Set custom DNS servers in the /etc/resolv.conf file that will be shared between all containers in the pod. A special option, “none” is allowed which disables creation of /etc/resolv.conf for the pod.
     */dns?: string,
    /**
     * Set custom DNS options in the /etc/resolv.conf file that will be shared between all containers in the pod.
     */dns_opt?: string,
    /**
     * Set custom DNS search domains in the /etc/resolv.conf file that will be shared between all containers in the pod.
     */dns_search?: string,
    /**
     * Generate systemd unit file for container.
     */generate_systemd?: MetaObject,
    /**
     * GID map for the user namespace. Using this flag will run the container with user namespace enabled. It conflicts with the `userns` and `subgidname` flags.
     */gidmap?: string,
    /**
     * Set a hostname to the pod
     */hostname?: string,
    /**
     * Create an infra container and associate it with the pod. An infra container is a lightweight container used to coordinate the shared kernel namespace of a pod. Default is true.
     */infra?: boolean,
    /**
     * The command that will be run to start the infra container. Default is “/pause”.
     */infra_command?: string,
    /**
     * Write the pid of the infra container’s conmon process to a file. As conmon runs in a separate process than Podman, this is necessary when using systemd to manage Podman containers and pods.
     */infra_conmon_pidfile?: string,
    /**
     * The name that will be used for the pod’s infra container.
     */infra_name?: string,
    /**
     * The image that will be created for the infra container. Default is “k8s.gcr.io/pause:3.1”.
     */infra_image?: string,
    /**
     * Set a static IP for the pod’s shared network.
     */ip?: string,
    /**
     * Add metadata to a pod, pass dictionary of label keys and values.
     */label?: MetaObject,
    /**
     * Read in a line delimited file of labels.
     */label_file?: string,
    /**
     * Set a static MAC address for the pod’s shared network.
     */mac_address?: string,
    /**
     * Assign a name to the pod.
     */name?: string,
    /**
     * Set network mode for the pod. Supported values are bridge (the default), host (do not create a network namespace, all containers in the pod will use the host’s network), or a list of names of CNI networks to join.
     */network?: string,
    /**
     * Add a network-scoped alias for the pod, setting the alias for all networks that the pod joins. To set a name only for a specific network, use the alias option as described under the -`network` option. Network aliases work only with the bridge networking mode. This option can be specified multiple times.
     */network_alias?: string,
    /**
     * Disable creation of /etc/hosts for the pod.
     */no_hosts?: boolean,
    /**
     * Set the PID mode for the pod. The default is to create a private PID namespace for the pod. Requires the PID namespace to be shared via `share` option.
     */pid?: string,
    /**
     * Write the pod ID to the file.
     */pod_id_file?: string,
    /**
     * Publish a port or range of ports from the pod to the host.
     */publish?: string,
    /**
     * Use with present and started states to force the re-creation of an existing pod.
     */recreate?: boolean,
    /**
     * A comma delimited list of kernel namespaces to share. If none or “” is specified, no namespaces will be shared. The namespaces to choose from are ipc, net, pid, user, uts.
     */share?: string,
    /**
     * This variable is set for state
     */state?: string,
    /**
     * Name for GID map from the /etc/subgid file. Using this flag will run the container with user namespace enabled. This flag conflicts with `userns` and `gidmap`.
     */subgidname?: string,
    /**
     * Name for UID map from the /etc/subuid file. Using this flag will run the container with user namespace enabled. This flag conflicts with `userns` and `uidmap`.
     */subuidname?: string,
    /**
     * Run the container in a new user namespace using the supplied mapping. This option conflicts with the `userns` and `subuidname` options. This option provides a way to map host UIDs to container UIDs. It can be passed several times to map different ranges.

     */uidmap?: string,
    /**
     * Set the user namespace mode for all the containers in a pod. It defaults to the PODMAN_USERNS environment variable. An empty value (“”) means user namespaces are disabled.
     */userns?: string,
    /**
     * Create a bind mount.
     */volume?: string,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * Saves podman image to tar file
 */
export interface PodmanSave  extends ClosedSoftwareModule  {
    /**
     * Compress tarball image layers when pushing to a directory using the ‘dir’ transport. (default is same compression type, compressed or uncompressed, as source)
     */compress?: boolean,
    /**
     * Destination file to write image to.
     */dest?: string,
    /**
     * Force saving to file even if it exists.
     */force?: boolean,
    /**
     * Save image to docker-archive, oci-archive (see containers-transports(5)), oci-dir (oci transport), or docker-dir (dir transport with v2s2 manifest type).
     */format?: string,
    /**
     * Image to save.
     */image?: string,
    /**
     * Allow for creating archives with more than one image. Additional names will be interpreted as images instead of tags. Only supported for docker-archive.
     */multi_image_archive?: boolean,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * Manage Podman secrets
 */
export interface PodmanSecret  extends ClosedSoftwareModule  {
    /**
     * The value of the secret. Required when state is present.
     */data?: string,
    /**
     * Override default secrets driver, currently podman uses file which is unencrypted.
     */driver?: string,
    /**
     * Driver-specific key-value options.
     */driver_opts?: MetaObject,
    /**
     * Use it when state is present to remove and recreate an existing secret.
     */force?: boolean,
    /**
     * The name of the secret.
     */name?: string,
    /**
     * Use it when state is present and secret with the same name already exists. If set to true, the secret will NOT be recreated and remains as is.
     */skip_existing?: boolean,
    /**
     * Whether to create or remove the named secret.
     */state?: string,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * Add an additional name to a local image
 */
export interface PodmanTag  extends ClosedSoftwareModule  {
    /**
     * Image to tag.
     */image?: string,
    /**
     * Additional names.
     */target_names?: string,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * Manage Podman Volumes
 */
export interface PodmanVolume  extends ClosedSoftwareModule  {
    /**
     * Return additional information which can be helpful for investigations.
     */debug?: boolean,
    /**
     * Specify volume driver name (default local).
     */driver?: string,
    /**
     * Add metadata to a pod volume (e.g., label com.example.key=value).
     */label?: MetaObject,
    /**
     * Name of volume.
     */name?: string,
    /**
     * Set driver specific options. For example ‘device=tpmfs’, ‘type=tmpfs’. UID and GID idempotency is not supported due to changes in podman.
     */options?: string,
    /**
     * Recreate volume even if exists.
     */recreate?: boolean,
    /**
     * State of volume, default ‘present’
     */state?: string,
    /**
     * Path to podman executable if it is not in the $PATH on the machine running podman
     */executable?: string,
}
/**
 * linkml:Any type is an experimental feature for allowing arbitrary objects
 */
export interface MetaObject  {
}
/**
 * A concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a ucs compatible KG can be considered both instances of ucs classes, and OWL classes in their own right. In general you should not need to use this class directly.  Instead, use the appropriate ucs class, i.e. cso:ComputationalProcess
 */
export interface OntologyClass  {
}
/**
 * Model root class for entity annotations.
 */
export interface Annotation  {
}
/**
 * A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric value
 */
export interface QuantityValue  extends Annotation  {
    /**
     * connects a quantity value to a unit
     */hasUnit?: string,
    /**
     * connects a quantity value to a number
     */hasNumericValue?: number,
}
/**
 * A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
 */
export interface Attribute  extends Annotation, OntologyClass  {
    /**
     * The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
     */name?: string,
    /**
     * connects an attribute to a class that describes it
     */hasAttributeType?: OntologyClass,
    /**
     * Connects an attribute to a value
     */hasQuantitativeValue?: QuantityValue[],
    /**
     * connects an attribute to a value
     */hasQualitativeValue?: NamedThingId,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Object (person, place, text, thing, etc.) from which something (information, goods, etc.) comes or is acquired
     */src?: string,
}
/**
 * Root Universal Model class for all things and informational relationships, real or imagined.
 */
export interface Entity  {
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * a databased entity or concept/class
 */
export interface NamedThing  extends Entity  {
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * A mixin that can be used on any entity that can be taxonomically classified. This includes individual entities, their products, and other operational entities and processes.
 */
export interface ThingWithTaxon  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
}
/**
 * Relating to the arrangements and work that is needed to control the operation of a plan
 */
export interface AdministrativeEntity  extends NamedThing  {
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * person, group, organization or project that provides a piece of information (i.e. a knowledge association)
 */
export interface Agent  extends AdministrativeEntity  {
    /**
     * a professional relationship between one provider (x) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
     */affiliation?: string,
    /**
     * Collection of information that describes the location of a building, apartment, or other structure
     */address?: string,
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * A piece of information that typically describes some topic of discourse or is used as support.
 */
export interface InformationContentEntity  extends NamedThing  {
    license?: string,
    rights?: string,
    format?: string,
    /**
     * date on which an entity was created. This can be applied to nodes or edges
     */creationDate?: date,
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Csolink category subclasses.
 */
export interface Publication  extends InformationContentEntity  {
    /**
     * Connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".
     */authors?: string,
    /**
     * Page number of source referenced for statement or publication
     */pages?: string,
    /**
     * executive  summary of a publication
     */summary?: string,
    /**
     * keywords tagging a publication
     */keywords?: string,
    /**
     * Library of Congress Subject Headings (LCSH) terms tagging a publication
     */lcshTerms?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    license?: string,
    rights?: string,
    format?: string,
    /**
     * date on which an entity was created. This can be applied to nodes or edges
     */creationDate?: date,
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Class of evidence that supports an association
 */
export interface EvidenceType  extends InformationContentEntity  {
    license?: string,
    rights?: string,
    format?: string,
    /**
     * date on which an entity was created. This can be applied to nodes or edges
     */creationDate?: date,
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Collaborative enterprise, frequently involving research or design, that is carefully planned to achieve a particular aim
 */
export interface Project  extends AdministrativeEntity  {
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * An entity that intends to perform some functions, interacting with other systems. Relative to a given system, the entities with which it interacts, are considered its environment. A system is structurally composed of a set of components bound together.
 */
export interface System  extends NamedThing, ThingWithTaxon  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Either software or hardware
 */
export interface SoftwareOrDevice  extends System  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * A set of instructions in a computer programming language that can be executed by a computer, possibly after compilation into another programming language. The term Software includes ComputerPrograms (free-standing software), object methods, subroutines and software packages.
 */
export interface Software  extends SoftwareOrDevice  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * physical components of a computer
 */
export interface Hardware  extends SoftwareOrDevice  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Philosophy about free redistribution and access to a product
 */
export interface OpenSource  {
}
/**
 * An operating system (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs.
 */
export interface OperatingSystem  extends Software  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Unix operating system originally developed by Sun Microsystems
 */
export interface Solaris  extends OperatingSystem  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * family of Unix-like operating systems using Linux kernel and open source
 */
export interface Linux  extends OperatingSystem, OpenSource  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * family of computer operating systems developed by Microsoft
 */
export interface Windows  extends OperatingSystem  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * computing technique for setting up virtual versions of operating systems or computer resources
 */
export interface Virtualization  {
}
/**
 * A typed association between two entities, supported by evidence
 */
export interface Association  extends Entity  {
    /**
     * Connects an association to the subject of the association. For example, in a apple-to-orange association, the apple is subject and orange is object.
     */subject?: NamedThingId,
    /**
     * A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     */predicate?: string,
    /**
     * Connects an association to the object of the association. For example, in a apple-to-orange assocation, the apple is subject and orange is object.
     */object?: NamedThingId,
    /**
     * if set to true, then the association is negated i.e. is not true
     */negated?: boolean,
    /**
     * connects an association to qualifiers that modify or qualify the meaning of that association
     */qualifiers?: OntologyClass[],
    /**
     * connects an association to publications supporting the association
     */publications?: PublicationId[],
    /**
     * connects an association to an instance of supporting evidence
     */hasEvidence?: EvidenceTypeId[],
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * rdf:type of ucs-core:Association should be fixed at rdf:Statement
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}

