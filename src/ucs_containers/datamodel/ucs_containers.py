# Auto generated from ucs_containers.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-14T02:08:57
# Schema: ucs-containers
#
# id: https://w3id.org/lmodel/ucs-containers
# description: Classes and Properties representing Containers in UseCaseS Framework
# license: Apache Software License 2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Double, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AML = CurieNamespace('AML', 'https://w3id.org/i40/aml#')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
BTO = CurieNamespace('BTO', 'http://purl.obolibrary.org/obo/BTO_')
CDAO = CurieNamespace('CDAO', 'http://purl.obolibrary.org/obo/CDAO_')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
CTRL = CurieNamespace('CTRL', 'https://w3id.org/ibp/CTRLont#')
DOI = CurieNamespace('DOI', 'http://identifiers.org/doi/')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
GR = CurieNamespace('GR', 'http://purl.org/goodrelations/v1#')
GSSO = CurieNamespace('GSSO', 'http://purl.obolibrary.org/obo/GSSO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
INO = CurieNamespace('INO', 'http://purl.obolibrary.org/obo/INO_')
LCSH = CurieNamespace('LCSH', 'http://id.loc.gov/authorities/subjects/')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
MS = CurieNamespace('MS', 'http://purl.obolibrary.org/obo/MS_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBAN = CurieNamespace('OBAN', 'http://purl.org/oban/')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
OM = CurieNamespace('OM', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
ONTOAVIDA = CurieNamespace('ONTOAVIDA', 'http://purl.obolibrary.org/obo/ONTOAVIDA_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
SAN = CurieNamespace('SAN', 'https://www.irit.fr/recherches/MELODI/ontologies/SAN.html#')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
SWO = CurieNamespace('SWO', 'http://purl.obolibrary.org/obo/SWO_')
T4FS = CurieNamespace('T4FS', 'http://purl.obolibrary.org/obo/T4FS_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
XAPI = CurieNamespace('XAPI', 'http://ns.inria.fr/ludo/v1/docs/xapi.html#')
AML = CurieNamespace('aml', 'https://w3id.org/i40/aml#')
CONTAINERS = CurieNamespace('containers', 'https://w3id.org/lmodel/ucs-containers/')
CORE = CurieNamespace('core', 'https://w3id.org/lmodel/ucs-core/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
CTRL = CurieNamespace('ctrl', 'https://w3id.org/ibp/CTRLont#')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DWC = CurieNamespace('dwc', 'https://dwc.tdwg.org/terms/#dc:')
EDAM_DATA = CurieNamespace('edam_data', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('edam_format', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('edam_operation', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('edam_topic', 'http://edamontology.org/topic_')
GEOLINK = CurieNamespace('geolink', 'http://schema.geolink.org/1.0/base/main.html#')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
GVP = CurieNamespace('gvp', 'http://vocab.getty.edu/ontology#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RR = CurieNamespace('rr', 'http://www.w3.org/ns/r2rml#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SCHEMA_UCS_CORE = CurieNamespace('schema_ucs_core', 'https://w3id.org/lmodel/ucs-core/schema/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'http://www.w3.org/ns/ssn/')
SSN_SYSTEM = CurieNamespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
UBERON = CurieNamespace('uberon', 'http://purl.obolibrary.org/obo/UBERON_')
UCO_CORE = CurieNamespace('uco-core', 'https://w3id.org/lmodel/uco-core/')
UCO_IDENTITY = CurieNamespace('uco-identity', 'https://w3id.org/lmodel/uco-identity/')
UCO_OBSERVABLE = CurieNamespace('uco-observable', 'https://w3id.org/lmodel/uco-observable/')
UCO_TYPES = CurieNamespace('uco-types', 'https://w3id.org/lmodel/uco-types/')
UCS_CORE = CurieNamespace('ucs-core', 'https://w3id.org/lmodel/ucs-core/')
WIKIDATA = CurieNamespace('wikidata', 'http://identifiers.org/wikidata/')
WIKIDATA_PROPERTY = CurieNamespace('wikidata_property', 'https://www.wikidata.org/wiki/Property:')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CONTAINERS


# Types
class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the universal model.  The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the universal class, for example universal:Service. For an RDF representation, the value should be a URI such as https://w3id.org/lmodel/base/vocab/Service """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = CONTAINERS.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = CONTAINERS.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = CONTAINERS.LabelType


class PredicateType(Uriorcurie):
    """ A CURIE from the csolink related_to hierarchy. For example, schema:related_to """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = CONTAINERS.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = CONTAINERS.NarrativeText


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = CONTAINERS.Unit


# Class references
class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class AgentId(AdministrativeEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class ProjectId(AdministrativeEntityId):
    pass


class OpenContainerInitiativeId(ProjectId):
    pass


class LinuxContainersProjectId(ProjectId):
    pass


class SystemId(NamedThingId):
    pass


class SoftwareOrDeviceId(SystemId):
    pass


class SoftwareId(SoftwareOrDeviceId):
    pass


class ContainerId(SoftwareId):
    pass


class LxcId(SoftwareId):
    pass


class LxcFsId(SoftwareId):
    pass


class LxdId(SoftwareId):
    pass


class OciContainerId(ContainerId):
    pass


class PodmanId(SoftwareId):
    pass


class ContainerdId(SoftwareId):
    pass


class DockerId(SoftwareId):
    pass


class KubernetesId(SoftwareId):
    pass


class HardwareId(SoftwareOrDeviceId):
    pass


class OperatingSystemId(SoftwareId):
    pass


class SolarisId(OperatingSystemId):
    pass


class LinuxId(OperatingSystemId):
    pass


class WindowsId(OperatingSystemId):
    pass


class AssociationId(EntityId):
    pass


class ClosedSoftwareModule(YAMLRoot):
    """
    Self contained software module
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.ClosedSoftwareModule
    class_class_curie: ClassVar[str] = "containers:ClosedSoftwareModule"
    class_name: ClassVar[str] = "ClosedSoftwareModule"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.ClosedSoftwareModule


@dataclass
class PodmanContainer(ClosedSoftwareModule):
    """
    Podman container
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanContainer
    class_class_curie: ClassVar[str] = "containers:PodmanContainer"
    class_name: ClassVar[str] = "PodmanContainer"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanContainer

    name: Union[str, LabelType] = None
    executable: Optional[str] = "podman"
    state: Optional[Union[str, "ContainerStateEnum"]] = "started"
    annotation: Optional[Union[dict, "MetaObject"]] = None
    authfile: Optional[str] = None
    blkio_weight: Optional[int] = None
    blkio_weight_device: Optional[Union[Union[dict, "MetaObject"], List[Union[dict, "MetaObject"]]]] = empty_list()
    cap_add: Optional[Union[str, List[str]]] = empty_list()
    cap_drop: Optional[Union[str, List[str]]] = empty_list()
    cgroup_parent: Optional[str] = None
    cgroupns: Optional[str] = None
    cgroups: Optional[str] = None
    cidfile: Optional[str] = None
    cmd_args: Optional[Union[str, List[str]]] = empty_list()
    conmon_pidfile: Optional[str] = None
    command: Optional[Union[str, List[str]]] = empty_list()
    cpu_period: Optional[int] = None
    cpu_rt_period: Optional[int] = None
    cpu_rt_runtime: Optional[int] = None
    cpu_shares: Optional[int] = None
    cpus: Optional[str] = None
    cpuset_cpus: Optional[str] = None
    cpuset_mems: Optional[str] = None
    detach: Optional[Union[bool, Bool]] = True
    debug: Optional[Union[bool, Bool]] = False
    detach_keys: Optional[str] = None
    device: Optional[Union[str, List[str]]] = empty_list()
    device_read_bps: Optional[Union[str, List[str]]] = empty_list()
    device_read_iops: Optional[Union[str, List[str]]] = empty_list()
    device_write_bps: Optional[Union[str, List[str]]] = empty_list()
    device_write_iops: Optional[Union[str, List[str]]] = empty_list()
    dns: Optional[Union[str, List[str]]] = empty_list()
    dns_option: Optional[str] = None
    dns_search: Optional[str] = None
    entrypoint: Optional[str] = None
    env: Optional[Union[dict, "MetaObject"]] = None
    env_file: Optional[str] = None
    env_host: Optional[Union[bool, Bool]] = False
    etc_hosts: Optional[Union[dict, "MetaObject"]] = None
    expose: Optional[Union[str, List[str]]] = empty_list()
    force_restart: Optional[Union[bool, Bool]] = False
    generate_systemd: Optional[Union[dict, "MetaObject"]] = None
    gidmap: Optional[Union[str, List[str]]] = empty_list()
    group_add: Optional[Union[str, List[str]]] = empty_list()
    healthcheck: Optional[str] = None
    healthcheck_interval: Optional[str] = None
    healthcheck_retries: Optional[int] = 3
    healthcheck_start_period: Optional[str] = "0s"
    healthcheck_timeout: Optional[str] = "30s"
    hostname: Optional[str] = None
    http_proxy: Optional[Union[bool, Bool]] = True
    image_volume: Optional[Union[str, "ContainerImageVolumeEnum"]] = None
    image_strict: Optional[Union[bool, Bool]] = False
    init: Optional[Union[bool, Bool]] = False
    init_path: Optional[str] = None
    interactive: Optional[Union[bool, Bool]] = False
    ip: Optional[str] = None
    ipc: Optional[str] = None
    kernel_memory: Optional[str] = None
    label: Optional[Union[dict, "MetaObject"]] = None
    label_file: Optional[str] = None
    log_driver: Optional[Union[str, "ContainerLogDriverEnum"]] = None
    log_level: Optional[Union[str, "ContainerLogLevelEnum"]] = None
    log_opt: Optional[Union[dict, "MetaObject"]] = None
    mac_address: Optional[str] = None
    memory: Optional[str] = None
    memory_reservation: Optional[str] = None
    memory_swap: Optional[str] = None
    memory_swappiness: Optional[int] = None
    mount: Optional[Union[str, List[str]]] = empty_list()
    network: Optional[Union[str, List[str]]] = empty_list()
    network_aliases: Optional[Union[str, List[str]]] = empty_list()
    no_hosts: Optional[Union[bool, Bool]] = False
    oom_kill_disable: Optional[Union[bool, Bool]] = False
    oom_score_adj: Optional[int] = None
    pid: Optional[str] = None
    pids_limit: Optional[int] = None
    pod: Optional[str] = None
    privileged: Optional[Union[bool, Bool]] = False
    publish: Optional[Union[str, List[str]]] = empty_list()
    publish_all: Optional[Union[bool, Bool]] = False
    read_only: Optional[Union[bool, Bool]] = False
    read_only_tmpfs: Optional[Union[bool, Bool]] = True
    recreate: Optional[Union[bool, Bool]] = False
    requires: Optional[Union[str, List[str]]] = empty_list()
    restart_policy: Optional[str] = None
    rm: Optional[Union[bool, Bool]] = False
    rootfs: Optional[Union[bool, Bool]] = False
    sdnotify: Optional[str] = None
    secrets: Optional[Union[str, List[str]]] = empty_list()
    security_opt: Optional[Union[str, List[str]]] = empty_list()
    shm_size: Optional[str] = None
    sig_proxy: Optional[Union[bool, Bool]] = True
    stop_signal: Optional[int] = None
    stop_timeout: Optional[int] = 10
    subgidname: Optional[str] = None
    subuidname: Optional[str] = None
    sysctl: Optional[Union[dict, "MetaObject"]] = None
    systemd: Optional[str] = "true"
    timezone: Optional[str] = None
    tmpfs: Optional[Union[dict, "MetaObject"]] = None
    tty: Optional[Union[bool, Bool]] = False
    uidmap: Optional[Union[str, List[str]]] = empty_list()
    ulimit: Optional[Union[str, List[str]]] = empty_list()
    user: Optional[str] = None
    userns: Optional[str] = None
    uts: Optional[str] = None
    volume: Optional[Union[str, List[str]]] = empty_list()
    volumes_from: Optional[Union[str, List[str]]] = empty_list()
    workdir: Optional[str] = None
    image: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if self.state is not None and not isinstance(self.state, ContainerStateEnum):
            self.state = ContainerStateEnum(self.state)

        if self.authfile is not None and not isinstance(self.authfile, str):
            self.authfile = str(self.authfile)

        if self.blkio_weight is not None and not isinstance(self.blkio_weight, int):
            self.blkio_weight = int(self.blkio_weight)

        if not isinstance(self.cap_add, list):
            self.cap_add = [self.cap_add] if self.cap_add is not None else []
        self.cap_add = [v if isinstance(v, str) else str(v) for v in self.cap_add]

        if not isinstance(self.cap_drop, list):
            self.cap_drop = [self.cap_drop] if self.cap_drop is not None else []
        self.cap_drop = [v if isinstance(v, str) else str(v) for v in self.cap_drop]

        if self.cgroup_parent is not None and not isinstance(self.cgroup_parent, str):
            self.cgroup_parent = str(self.cgroup_parent)

        if self.cgroupns is not None and not isinstance(self.cgroupns, str):
            self.cgroupns = str(self.cgroupns)

        if self.cgroups is not None and not isinstance(self.cgroups, str):
            self.cgroups = str(self.cgroups)

        if self.cidfile is not None and not isinstance(self.cidfile, str):
            self.cidfile = str(self.cidfile)

        if not isinstance(self.cmd_args, list):
            self.cmd_args = [self.cmd_args] if self.cmd_args is not None else []
        self.cmd_args = [v if isinstance(v, str) else str(v) for v in self.cmd_args]

        if self.conmon_pidfile is not None and not isinstance(self.conmon_pidfile, str):
            self.conmon_pidfile = str(self.conmon_pidfile)

        if not isinstance(self.command, list):
            self.command = [self.command] if self.command is not None else []
        self.command = [v if isinstance(v, str) else str(v) for v in self.command]

        if self.cpu_period is not None and not isinstance(self.cpu_period, int):
            self.cpu_period = int(self.cpu_period)

        if self.cpu_rt_period is not None and not isinstance(self.cpu_rt_period, int):
            self.cpu_rt_period = int(self.cpu_rt_period)

        if self.cpu_rt_runtime is not None and not isinstance(self.cpu_rt_runtime, int):
            self.cpu_rt_runtime = int(self.cpu_rt_runtime)

        if self.cpu_shares is not None and not isinstance(self.cpu_shares, int):
            self.cpu_shares = int(self.cpu_shares)

        if self.cpus is not None and not isinstance(self.cpus, str):
            self.cpus = str(self.cpus)

        if self.cpuset_cpus is not None and not isinstance(self.cpuset_cpus, str):
            self.cpuset_cpus = str(self.cpuset_cpus)

        if self.cpuset_mems is not None and not isinstance(self.cpuset_mems, str):
            self.cpuset_mems = str(self.cpuset_mems)

        if self.detach is not None and not isinstance(self.detach, Bool):
            self.detach = Bool(self.detach)

        if self.debug is not None and not isinstance(self.debug, Bool):
            self.debug = Bool(self.debug)

        if self.detach_keys is not None and not isinstance(self.detach_keys, str):
            self.detach_keys = str(self.detach_keys)

        if not isinstance(self.device, list):
            self.device = [self.device] if self.device is not None else []
        self.device = [v if isinstance(v, str) else str(v) for v in self.device]

        if not isinstance(self.device_read_bps, list):
            self.device_read_bps = [self.device_read_bps] if self.device_read_bps is not None else []
        self.device_read_bps = [v if isinstance(v, str) else str(v) for v in self.device_read_bps]

        if not isinstance(self.device_read_iops, list):
            self.device_read_iops = [self.device_read_iops] if self.device_read_iops is not None else []
        self.device_read_iops = [v if isinstance(v, str) else str(v) for v in self.device_read_iops]

        if not isinstance(self.device_write_bps, list):
            self.device_write_bps = [self.device_write_bps] if self.device_write_bps is not None else []
        self.device_write_bps = [v if isinstance(v, str) else str(v) for v in self.device_write_bps]

        if not isinstance(self.device_write_iops, list):
            self.device_write_iops = [self.device_write_iops] if self.device_write_iops is not None else []
        self.device_write_iops = [v if isinstance(v, str) else str(v) for v in self.device_write_iops]

        if not isinstance(self.dns, list):
            self.dns = [self.dns] if self.dns is not None else []
        self.dns = [v if isinstance(v, str) else str(v) for v in self.dns]

        if self.dns_option is not None and not isinstance(self.dns_option, str):
            self.dns_option = str(self.dns_option)

        if self.dns_search is not None and not isinstance(self.dns_search, str):
            self.dns_search = str(self.dns_search)

        if self.entrypoint is not None and not isinstance(self.entrypoint, str):
            self.entrypoint = str(self.entrypoint)

        if self.env_file is not None and not isinstance(self.env_file, str):
            self.env_file = str(self.env_file)

        if self.env_host is not None and not isinstance(self.env_host, Bool):
            self.env_host = Bool(self.env_host)

        if not isinstance(self.expose, list):
            self.expose = [self.expose] if self.expose is not None else []
        self.expose = [v if isinstance(v, str) else str(v) for v in self.expose]

        if self.force_restart is not None and not isinstance(self.force_restart, Bool):
            self.force_restart = Bool(self.force_restart)

        if not isinstance(self.gidmap, list):
            self.gidmap = [self.gidmap] if self.gidmap is not None else []
        self.gidmap = [v if isinstance(v, str) else str(v) for v in self.gidmap]

        if not isinstance(self.group_add, list):
            self.group_add = [self.group_add] if self.group_add is not None else []
        self.group_add = [v if isinstance(v, str) else str(v) for v in self.group_add]

        if self.healthcheck is not None and not isinstance(self.healthcheck, str):
            self.healthcheck = str(self.healthcheck)

        if self.healthcheck_interval is not None and not isinstance(self.healthcheck_interval, str):
            self.healthcheck_interval = str(self.healthcheck_interval)

        if self.healthcheck_retries is not None and not isinstance(self.healthcheck_retries, int):
            self.healthcheck_retries = int(self.healthcheck_retries)

        if self.healthcheck_start_period is not None and not isinstance(self.healthcheck_start_period, str):
            self.healthcheck_start_period = str(self.healthcheck_start_period)

        if self.healthcheck_timeout is not None and not isinstance(self.healthcheck_timeout, str):
            self.healthcheck_timeout = str(self.healthcheck_timeout)

        if self.hostname is not None and not isinstance(self.hostname, str):
            self.hostname = str(self.hostname)

        if self.http_proxy is not None and not isinstance(self.http_proxy, Bool):
            self.http_proxy = Bool(self.http_proxy)

        if self.image_volume is not None and not isinstance(self.image_volume, ContainerImageVolumeEnum):
            self.image_volume = ContainerImageVolumeEnum(self.image_volume)

        if self.image_strict is not None and not isinstance(self.image_strict, Bool):
            self.image_strict = Bool(self.image_strict)

        if self.init is not None and not isinstance(self.init, Bool):
            self.init = Bool(self.init)

        if self.init_path is not None and not isinstance(self.init_path, str):
            self.init_path = str(self.init_path)

        if self.interactive is not None and not isinstance(self.interactive, Bool):
            self.interactive = Bool(self.interactive)

        if self.ip is not None and not isinstance(self.ip, str):
            self.ip = str(self.ip)

        if self.ipc is not None and not isinstance(self.ipc, str):
            self.ipc = str(self.ipc)

        if self.kernel_memory is not None and not isinstance(self.kernel_memory, str):
            self.kernel_memory = str(self.kernel_memory)

        if self.label_file is not None and not isinstance(self.label_file, str):
            self.label_file = str(self.label_file)

        if self.log_driver is not None and not isinstance(self.log_driver, ContainerLogDriverEnum):
            self.log_driver = ContainerLogDriverEnum(self.log_driver)

        if self.log_level is not None and not isinstance(self.log_level, ContainerLogLevelEnum):
            self.log_level = ContainerLogLevelEnum(self.log_level)

        if self.mac_address is not None and not isinstance(self.mac_address, str):
            self.mac_address = str(self.mac_address)

        if self.memory is not None and not isinstance(self.memory, str):
            self.memory = str(self.memory)

        if self.memory_reservation is not None and not isinstance(self.memory_reservation, str):
            self.memory_reservation = str(self.memory_reservation)

        if self.memory_swap is not None and not isinstance(self.memory_swap, str):
            self.memory_swap = str(self.memory_swap)

        if self.memory_swappiness is not None and not isinstance(self.memory_swappiness, int):
            self.memory_swappiness = int(self.memory_swappiness)

        if not isinstance(self.mount, list):
            self.mount = [self.mount] if self.mount is not None else []
        self.mount = [v if isinstance(v, str) else str(v) for v in self.mount]

        if not isinstance(self.network, list):
            self.network = [self.network] if self.network is not None else []
        self.network = [v if isinstance(v, str) else str(v) for v in self.network]

        if not isinstance(self.network_aliases, list):
            self.network_aliases = [self.network_aliases] if self.network_aliases is not None else []
        self.network_aliases = [v if isinstance(v, str) else str(v) for v in self.network_aliases]

        if self.no_hosts is not None and not isinstance(self.no_hosts, Bool):
            self.no_hosts = Bool(self.no_hosts)

        if self.oom_kill_disable is not None and not isinstance(self.oom_kill_disable, Bool):
            self.oom_kill_disable = Bool(self.oom_kill_disable)

        if self.oom_score_adj is not None and not isinstance(self.oom_score_adj, int):
            self.oom_score_adj = int(self.oom_score_adj)

        if self.pid is not None and not isinstance(self.pid, str):
            self.pid = str(self.pid)

        if self.pids_limit is not None and not isinstance(self.pids_limit, int):
            self.pids_limit = int(self.pids_limit)

        if self.pod is not None and not isinstance(self.pod, str):
            self.pod = str(self.pod)

        if self.privileged is not None and not isinstance(self.privileged, Bool):
            self.privileged = Bool(self.privileged)

        if not isinstance(self.publish, list):
            self.publish = [self.publish] if self.publish is not None else []
        self.publish = [v if isinstance(v, str) else str(v) for v in self.publish]

        if self.publish_all is not None and not isinstance(self.publish_all, Bool):
            self.publish_all = Bool(self.publish_all)

        if self.read_only is not None and not isinstance(self.read_only, Bool):
            self.read_only = Bool(self.read_only)

        if self.read_only_tmpfs is not None and not isinstance(self.read_only_tmpfs, Bool):
            self.read_only_tmpfs = Bool(self.read_only_tmpfs)

        if self.recreate is not None and not isinstance(self.recreate, Bool):
            self.recreate = Bool(self.recreate)

        if not isinstance(self.requires, list):
            self.requires = [self.requires] if self.requires is not None else []
        self.requires = [v if isinstance(v, str) else str(v) for v in self.requires]

        if self.restart_policy is not None and not isinstance(self.restart_policy, str):
            self.restart_policy = str(self.restart_policy)

        if self.rm is not None and not isinstance(self.rm, Bool):
            self.rm = Bool(self.rm)

        if self.rootfs is not None and not isinstance(self.rootfs, Bool):
            self.rootfs = Bool(self.rootfs)

        if self.sdnotify is not None and not isinstance(self.sdnotify, str):
            self.sdnotify = str(self.sdnotify)

        if not isinstance(self.secrets, list):
            self.secrets = [self.secrets] if self.secrets is not None else []
        self.secrets = [v if isinstance(v, str) else str(v) for v in self.secrets]

        if not isinstance(self.security_opt, list):
            self.security_opt = [self.security_opt] if self.security_opt is not None else []
        self.security_opt = [v if isinstance(v, str) else str(v) for v in self.security_opt]

        if self.shm_size is not None and not isinstance(self.shm_size, str):
            self.shm_size = str(self.shm_size)

        if self.sig_proxy is not None and not isinstance(self.sig_proxy, Bool):
            self.sig_proxy = Bool(self.sig_proxy)

        if self.stop_signal is not None and not isinstance(self.stop_signal, int):
            self.stop_signal = int(self.stop_signal)

        if self.stop_timeout is not None and not isinstance(self.stop_timeout, int):
            self.stop_timeout = int(self.stop_timeout)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        if self.subgidname is not None and not isinstance(self.subgidname, str):
            self.subgidname = str(self.subgidname)

        if self.subuidname is not None and not isinstance(self.subuidname, str):
            self.subuidname = str(self.subuidname)

        if self.systemd is not None and not isinstance(self.systemd, str):
            self.systemd = str(self.systemd)

        if self.timezone is not None and not isinstance(self.timezone, str):
            self.timezone = str(self.timezone)

        if self.tty is not None and not isinstance(self.tty, Bool):
            self.tty = Bool(self.tty)

        if not isinstance(self.uidmap, list):
            self.uidmap = [self.uidmap] if self.uidmap is not None else []
        self.uidmap = [v if isinstance(v, str) else str(v) for v in self.uidmap]

        if not isinstance(self.ulimit, list):
            self.ulimit = [self.ulimit] if self.ulimit is not None else []
        self.ulimit = [v if isinstance(v, str) else str(v) for v in self.ulimit]

        if self.user is not None and not isinstance(self.user, str):
            self.user = str(self.user)

        if self.userns is not None and not isinstance(self.userns, str):
            self.userns = str(self.userns)

        if self.uts is not None and not isinstance(self.uts, str):
            self.uts = str(self.uts)

        if not isinstance(self.volume, list):
            self.volume = [self.volume] if self.volume is not None else []
        self.volume = [v if isinstance(v, str) else str(v) for v in self.volume]

        if not isinstance(self.volumes_from, list):
            self.volumes_from = [self.volumes_from] if self.volumes_from is not None else []
        self.volumes_from = [v if isinstance(v, str) else str(v) for v in self.volumes_from]

        if self.workdir is not None and not isinstance(self.workdir, str):
            self.workdir = str(self.workdir)

        if self.image is not None and not isinstance(self.image, str):
            self.image = str(self.image)

        super().__post_init__(**kwargs)


@dataclass
class PodmanContainers(ClosedSoftwareModule):
    """
    Podman containers
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanContainers
    class_class_curie: ClassVar[str] = "containers:PodmanContainers"
    class_name: ClassVar[str] = "PodmanContainers"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanContainers

    containers: Union[Union[dict, "MetaObject"], List[Union[dict, "MetaObject"]]] = None
    debug: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.debug is not None and not isinstance(self.debug, Bool):
            self.debug = Bool(self.debug)

        super().__post_init__(**kwargs)


@dataclass
class PodmanExport(ClosedSoftwareModule):
    """
    Export a Podman container
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanExport
    class_class_curie: ClassVar[str] = "containers:PodmanExport"
    class_name: ClassVar[str] = "PodmanExport"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanExport

    container: str = None
    dest: str = None
    executable: Optional[str] = "podman"
    force: Optional[Union[bool, Bool]] = True

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.container):
            self.MissingRequiredField("container")
        if not isinstance(self.container, str):
            self.container = str(self.container)

        if self._is_empty(self.dest):
            self.MissingRequiredField("dest")
        if not isinstance(self.dest, str):
            self.dest = str(self.dest)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if self.force is not None and not isinstance(self.force, Bool):
            self.force = Bool(self.force)

        super().__post_init__(**kwargs)


@dataclass
class PodmanGenerateSystemd(ClosedSoftwareModule):
    """
    Generate systemd unit from a pod or a container
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanGenerateSystemd
    class_class_curie: ClassVar[str] = "containers:PodmanGenerateSystemd"
    class_name: ClassVar[str] = "PodmanGenerateSystemd"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanGenerateSystemd

    name: Union[str, LabelType] = None
    after: Optional[Union[str, List[str]]] = empty_list()
    container_prefix: Optional[str] = None
    dest: Optional[str] = None
    env: Optional[Union[dict, "MetaObject"]] = None
    executable: Optional[str] = "podman"
    new: Optional[Union[bool, Bool]] = False
    no_header: Optional[Union[bool, Bool]] = False
    pod_prefix: Optional[str] = None
    requires: Optional[Union[str, List[str]]] = empty_list()
    restart_policy: Optional[Union[str, "ContainerRestartPolicyEnum"]] = None
    restart_sec: Optional[int] = None
    separator: Optional[str] = None
    start_timeout: Optional[int] = None
    stop_timeout: Optional[int] = None
    use_names: Optional[Union[bool, Bool]] = True
    wants: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.after, list):
            self.after = [self.after] if self.after is not None else []
        self.after = [v if isinstance(v, str) else str(v) for v in self.after]

        if self.container_prefix is not None and not isinstance(self.container_prefix, str):
            self.container_prefix = str(self.container_prefix)

        if self.dest is not None and not isinstance(self.dest, str):
            self.dest = str(self.dest)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if self.new is not None and not isinstance(self.new, Bool):
            self.new = Bool(self.new)

        if self.no_header is not None and not isinstance(self.no_header, Bool):
            self.no_header = Bool(self.no_header)

        if self.pod_prefix is not None and not isinstance(self.pod_prefix, str):
            self.pod_prefix = str(self.pod_prefix)

        if not isinstance(self.requires, list):
            self.requires = [self.requires] if self.requires is not None else []
        self.requires = [v if isinstance(v, str) else str(v) for v in self.requires]

        if self.restart_policy is not None and not isinstance(self.restart_policy, ContainerRestartPolicyEnum):
            self.restart_policy = ContainerRestartPolicyEnum(self.restart_policy)

        if self.restart_sec is not None and not isinstance(self.restart_sec, int):
            self.restart_sec = int(self.restart_sec)

        if self.separator is not None and not isinstance(self.separator, str):
            self.separator = str(self.separator)

        if self.start_timeout is not None and not isinstance(self.start_timeout, int):
            self.start_timeout = int(self.start_timeout)

        if self.stop_timeout is not None and not isinstance(self.stop_timeout, int):
            self.stop_timeout = int(self.stop_timeout)

        if self.use_names is not None and not isinstance(self.use_names, Bool):
            self.use_names = Bool(self.use_names)

        if not isinstance(self.wants, list):
            self.wants = [self.wants] if self.wants is not None else []
        self.wants = [v if isinstance(v, str) else str(v) for v in self.wants]

        super().__post_init__(**kwargs)


@dataclass
class PodmanImage(ClosedSoftwareModule):
    """
    Podman container image
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanImage
    class_class_curie: ClassVar[str] = "containers:PodmanImage"
    class_name: ClassVar[str] = "PodmanImage"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanImage

    name: Union[str, LabelType] = None
    auth_file: Optional[str] = None
    build: Optional[Union[dict, "MetaObject"]] = None
    ca_cert_dir: Optional[str] = None
    executable: Optional[str] = "podman"
    force: Optional[Union[bool, Bool]] = False
    password: Optional[str] = None
    path: Optional[str] = None
    pull: Optional[Union[bool, Bool]] = True
    push: Optional[Union[bool, Bool]] = False
    push_args: Optional[Union[dict, "MetaObject"]] = None
    compress: Optional[str] = None
    dest: Optional[str] = None
    format: Optional[str] = None
    remove_signatures: Optional[str] = None
    sign_by: Optional[str] = None
    transport: Optional[str] = None
    state: Optional[Union[str, "ContainerImageStateEnum"]] = "present"
    tag: Optional[str] = "latest"
    username: Optional[str] = None
    validate_certs: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.auth_file is not None and not isinstance(self.auth_file, str):
            self.auth_file = str(self.auth_file)

        if self.ca_cert_dir is not None and not isinstance(self.ca_cert_dir, str):
            self.ca_cert_dir = str(self.ca_cert_dir)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if self.force is not None and not isinstance(self.force, Bool):
            self.force = Bool(self.force)

        if self.password is not None and not isinstance(self.password, str):
            self.password = str(self.password)

        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        if self.pull is not None and not isinstance(self.pull, Bool):
            self.pull = Bool(self.pull)

        if self.push is not None and not isinstance(self.push, Bool):
            self.push = Bool(self.push)

        if self.compress is not None and not isinstance(self.compress, str):
            self.compress = str(self.compress)

        if self.dest is not None and not isinstance(self.dest, str):
            self.dest = str(self.dest)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.remove_signatures is not None and not isinstance(self.remove_signatures, str):
            self.remove_signatures = str(self.remove_signatures)

        if self.sign_by is not None and not isinstance(self.sign_by, str):
            self.sign_by = str(self.sign_by)

        if self.transport is not None and not isinstance(self.transport, str):
            self.transport = str(self.transport)

        if self.state is not None and not isinstance(self.state, ContainerImageStateEnum):
            self.state = ContainerImageStateEnum(self.state)

        if self.tag is not None and not isinstance(self.tag, str):
            self.tag = str(self.tag)

        if self.username is not None and not isinstance(self.username, str):
            self.username = str(self.username)

        if self.validate_certs is not None and not isinstance(self.validate_certs, Bool):
            self.validate_certs = Bool(self.validate_certs)

        super().__post_init__(**kwargs)


@dataclass
class PodmanImport(ClosedSoftwareModule):
    """
    Import Podman container from file
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanImport
    class_class_curie: ClassVar[str] = "containers:PodmanImport"
    class_name: ClassVar[str] = "PodmanImport"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanImport

    src: str = None
    change: Optional[Union[Union[dict, "MetaObject"], List[Union[dict, "MetaObject"]]]] = empty_list()
    commit_message: Optional[str] = None
    executable: Optional[str] = "podman"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.src):
            self.MissingRequiredField("src")
        if not isinstance(self.src, str):
            self.src = str(self.src)

        if self.commit_message is not None and not isinstance(self.commit_message, str):
            self.commit_message = str(self.commit_message)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        super().__post_init__(**kwargs)


@dataclass
class PodmanLoad(ClosedSoftwareModule):
    """
    Load container into container storage
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanLoad
    class_class_curie: ClassVar[str] = "containers:PodmanLoad"
    class_name: ClassVar[str] = "PodmanLoad"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanLoad

    input: str = None
    executable: Optional[str] = "podman"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.input):
            self.MissingRequiredField("input")
        if not isinstance(self.input, str):
            self.input = str(self.input)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        super().__post_init__(**kwargs)


@dataclass
class PodmanLogin(ClosedSoftwareModule):
    """
    Login to a Container registry using Podman
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanLogin
    class_class_curie: ClassVar[str] = "containers:PodmanLogin"
    class_name: ClassVar[str] = "PodmanLogin"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanLogin

    password: str = None
    username: str = None
    authfile: Optional[str] = None
    certdir: Optional[str] = None
    executable: Optional[str] = "podman"
    registry: Optional[str] = None
    tlsverify: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.password):
            self.MissingRequiredField("password")
        if not isinstance(self.password, str):
            self.password = str(self.password)

        if self._is_empty(self.username):
            self.MissingRequiredField("username")
        if not isinstance(self.username, str):
            self.username = str(self.username)

        if self.authfile is not None and not isinstance(self.authfile, str):
            self.authfile = str(self.authfile)

        if self.certdir is not None and not isinstance(self.certdir, str):
            self.certdir = str(self.certdir)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if self.registry is not None and not isinstance(self.registry, str):
            self.registry = str(self.registry)

        if self.tlsverify is not None and not isinstance(self.tlsverify, Bool):
            self.tlsverify = Bool(self.tlsverify)

        super().__post_init__(**kwargs)


@dataclass
class PodmanLogout(ClosedSoftwareModule):
    """
    Logout of a Container registry using Podman
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanLogout
    class_class_curie: ClassVar[str] = "containers:PodmanLogout"
    class_name: ClassVar[str] = "PodmanLogout"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanLogout

    all: Optional[Union[bool, Bool]] = None
    authfile: Optional[str] = None
    executable: Optional[str] = "podman"
    ignore_docker_credentials: Optional[Union[bool, Bool]] = None
    registry: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.all is not None and not isinstance(self.all, Bool):
            self.all = Bool(self.all)

        if self.authfile is not None and not isinstance(self.authfile, str):
            self.authfile = str(self.authfile)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if self.ignore_docker_credentials is not None and not isinstance(self.ignore_docker_credentials, Bool):
            self.ignore_docker_credentials = Bool(self.ignore_docker_credentials)

        if self.registry is not None and not isinstance(self.registry, str):
            self.registry = str(self.registry)

        super().__post_init__(**kwargs)


@dataclass
class PodmanNetwork(ClosedSoftwareModule):
    """
    Manage podman networks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanNetwork
    class_class_curie: ClassVar[str] = "containers:PodmanNetwork"
    class_name: ClassVar[str] = "PodmanNetwork"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanNetwork

    name: Union[str, LabelType] = None
    debug: Optional[Union[bool, Bool]] = False
    disable_dns: Optional[Union[bool, Bool]] = False
    driver: Optional[str] = None
    executable: Optional[str] = None
    gateway: Optional[str] = None
    internal: Optional[Union[bool, Bool]] = None
    ip_range: Optional[str] = None
    ipv6: Optional[Union[bool, Bool]] = None
    macvlan: Optional[str] = None
    opt: Optional[Union[dict, "MetaObject"]] = None
    recreate: Optional[Union[bool, Bool]] = False
    state: Optional[Union[str, "ContainerNetworkStateEnum"]] = "present"
    subnet: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.debug is not None and not isinstance(self.debug, Bool):
            self.debug = Bool(self.debug)

        if self.disable_dns is not None and not isinstance(self.disable_dns, Bool):
            self.disable_dns = Bool(self.disable_dns)

        if self.driver is not None and not isinstance(self.driver, str):
            self.driver = str(self.driver)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if self.gateway is not None and not isinstance(self.gateway, str):
            self.gateway = str(self.gateway)

        if self.internal is not None and not isinstance(self.internal, Bool):
            self.internal = Bool(self.internal)

        if self.ip_range is not None and not isinstance(self.ip_range, str):
            self.ip_range = str(self.ip_range)

        if self.ipv6 is not None and not isinstance(self.ipv6, Bool):
            self.ipv6 = Bool(self.ipv6)

        if self.macvlan is not None and not isinstance(self.macvlan, str):
            self.macvlan = str(self.macvlan)

        if self.recreate is not None and not isinstance(self.recreate, Bool):
            self.recreate = Bool(self.recreate)

        if self.state is not None and not isinstance(self.state, ContainerNetworkStateEnum):
            self.state = ContainerNetworkStateEnum(self.state)

        if self.subnet is not None and not isinstance(self.subnet, str):
            self.subnet = str(self.subnet)

        super().__post_init__(**kwargs)


@dataclass
class PodmanPlay(ClosedSoftwareModule):
    """
    Play kubernetes YAML file using podman
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanPlay
    class_class_curie: ClassVar[str] = "containers:PodmanPlay"
    class_name: ClassVar[str] = "PodmanPlay"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanPlay

    kube_file: str = None
    state: Union[str, "ContainerStateEnum"] = None
    authfile: Optional[str] = None
    cert_dir: Optional[str] = None
    configmap: Optional[Union[str, List[str]]] = empty_list()
    debug: Optional[Union[bool, Bool]] = None
    executable: Optional[str] = None
    log_driver: Optional[str] = None
    log_level: Optional[Union[str, "ContainerLogLevelEnum"]] = None
    network: Optional[Union[str, List[str]]] = empty_list()
    password: Optional[str] = None
    quiet: Optional[Union[bool, Bool]] = None
    recreate: Optional[Union[bool, Bool]] = False
    seccomp_profile_root: Optional[str] = None
    tls_verify: Optional[Union[bool, Bool]] = None
    username: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.kube_file):
            self.MissingRequiredField("kube_file")
        if not isinstance(self.kube_file, str):
            self.kube_file = str(self.kube_file)

        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, ContainerStateEnum):
            self.state = ContainerStateEnum(self.state)

        if self.authfile is not None and not isinstance(self.authfile, str):
            self.authfile = str(self.authfile)

        if self.cert_dir is not None and not isinstance(self.cert_dir, str):
            self.cert_dir = str(self.cert_dir)

        if not isinstance(self.configmap, list):
            self.configmap = [self.configmap] if self.configmap is not None else []
        self.configmap = [v if isinstance(v, str) else str(v) for v in self.configmap]

        if self.debug is not None and not isinstance(self.debug, Bool):
            self.debug = Bool(self.debug)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if self.log_driver is not None and not isinstance(self.log_driver, str):
            self.log_driver = str(self.log_driver)

        if self.log_level is not None and not isinstance(self.log_level, ContainerLogLevelEnum):
            self.log_level = ContainerLogLevelEnum(self.log_level)

        if not isinstance(self.network, list):
            self.network = [self.network] if self.network is not None else []
        self.network = [v if isinstance(v, str) else str(v) for v in self.network]

        if self.password is not None and not isinstance(self.password, str):
            self.password = str(self.password)

        if self.quiet is not None and not isinstance(self.quiet, Bool):
            self.quiet = Bool(self.quiet)

        if self.recreate is not None and not isinstance(self.recreate, Bool):
            self.recreate = Bool(self.recreate)

        if self.seccomp_profile_root is not None and not isinstance(self.seccomp_profile_root, str):
            self.seccomp_profile_root = str(self.seccomp_profile_root)

        if self.tls_verify is not None and not isinstance(self.tls_verify, Bool):
            self.tls_verify = Bool(self.tls_verify)

        if self.username is not None and not isinstance(self.username, str):
            self.username = str(self.username)

        super().__post_init__(**kwargs)


@dataclass
class PodmanPod(ClosedSoftwareModule):
    """
    Manage Podman pods
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanPod
    class_class_curie: ClassVar[str] = "containers:PodmanPod"
    class_name: ClassVar[str] = "PodmanPod"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanPod

    name: Union[str, LabelType] = None
    add_host: Optional[Union[str, List[str]]] = empty_list()
    cgroup_parent: Optional[str] = None
    cpus: Optional[str] = None
    cpuset_cpus: Optional[str] = None
    debug: Optional[Union[bool, Bool]] = False
    device: Optional[Union[str, List[str]]] = empty_list()
    device_read_bps: Optional[Union[str, List[str]]] = empty_list()
    dns: Optional[Union[str, List[str]]] = empty_list()
    dns_opt: Optional[Union[str, List[str]]] = empty_list()
    dns_search: Optional[Union[str, List[str]]] = empty_list()
    executable: Optional[str] = "podman"
    generate_systemd: Optional[Union[dict, "MetaObject"]] = None
    gidmap: Optional[Union[str, List[str]]] = empty_list()
    hostname: Optional[str] = None
    infra: Optional[Union[bool, Bool]] = True
    infra_command: Optional[str] = None
    infra_conmon_pidfile: Optional[str] = None
    infra_name: Optional[str] = None
    infra_image: Optional[str] = "k8s.gcr.io/pause:3.1"
    ip: Optional[str] = None
    label: Optional[Union[dict, "MetaObject"]] = None
    label_file: Optional[str] = None
    mac_address: Optional[str] = None
    network: Optional[Union[str, List[str]]] = empty_list()
    network_alias: Optional[Union[str, List[str]]] = empty_list()
    no_hosts: Optional[Union[bool, Bool]] = True
    pid: Optional[str] = None
    pod_id_file: Optional[str] = None
    publish: Optional[Union[str, List[str]]] = empty_list()
    recreate: Optional[Union[bool, Bool]] = False
    share: Optional[str] = None
    state: Optional[Union[str, "ContainerStateEnum"]] = None
    subgidname: Optional[str] = None
    subuidname: Optional[str] = None
    uidmap: Optional[Union[str, List[str]]] = empty_list()
    userns: Optional[str] = None
    volume: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.add_host, list):
            self.add_host = [self.add_host] if self.add_host is not None else []
        self.add_host = [v if isinstance(v, str) else str(v) for v in self.add_host]

        if self.cgroup_parent is not None and not isinstance(self.cgroup_parent, str):
            self.cgroup_parent = str(self.cgroup_parent)

        if self.cpus is not None and not isinstance(self.cpus, str):
            self.cpus = str(self.cpus)

        if self.cpuset_cpus is not None and not isinstance(self.cpuset_cpus, str):
            self.cpuset_cpus = str(self.cpuset_cpus)

        if self.debug is not None and not isinstance(self.debug, Bool):
            self.debug = Bool(self.debug)

        if not isinstance(self.device, list):
            self.device = [self.device] if self.device is not None else []
        self.device = [v if isinstance(v, str) else str(v) for v in self.device]

        if not isinstance(self.device_read_bps, list):
            self.device_read_bps = [self.device_read_bps] if self.device_read_bps is not None else []
        self.device_read_bps = [v if isinstance(v, str) else str(v) for v in self.device_read_bps]

        if not isinstance(self.dns, list):
            self.dns = [self.dns] if self.dns is not None else []
        self.dns = [v if isinstance(v, str) else str(v) for v in self.dns]

        if not isinstance(self.dns_opt, list):
            self.dns_opt = [self.dns_opt] if self.dns_opt is not None else []
        self.dns_opt = [v if isinstance(v, str) else str(v) for v in self.dns_opt]

        if not isinstance(self.dns_search, list):
            self.dns_search = [self.dns_search] if self.dns_search is not None else []
        self.dns_search = [v if isinstance(v, str) else str(v) for v in self.dns_search]

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if not isinstance(self.gidmap, list):
            self.gidmap = [self.gidmap] if self.gidmap is not None else []
        self.gidmap = [v if isinstance(v, str) else str(v) for v in self.gidmap]

        if self.hostname is not None and not isinstance(self.hostname, str):
            self.hostname = str(self.hostname)

        if self.infra is not None and not isinstance(self.infra, Bool):
            self.infra = Bool(self.infra)

        if self.infra_command is not None and not isinstance(self.infra_command, str):
            self.infra_command = str(self.infra_command)

        if self.infra_conmon_pidfile is not None and not isinstance(self.infra_conmon_pidfile, str):
            self.infra_conmon_pidfile = str(self.infra_conmon_pidfile)

        if self.infra_name is not None and not isinstance(self.infra_name, str):
            self.infra_name = str(self.infra_name)

        if self.infra_image is not None and not isinstance(self.infra_image, str):
            self.infra_image = str(self.infra_image)

        if self.ip is not None and not isinstance(self.ip, str):
            self.ip = str(self.ip)

        if self.label_file is not None and not isinstance(self.label_file, str):
            self.label_file = str(self.label_file)

        if self.mac_address is not None and not isinstance(self.mac_address, str):
            self.mac_address = str(self.mac_address)

        if not isinstance(self.network, list):
            self.network = [self.network] if self.network is not None else []
        self.network = [v if isinstance(v, str) else str(v) for v in self.network]

        if not isinstance(self.network_alias, list):
            self.network_alias = [self.network_alias] if self.network_alias is not None else []
        self.network_alias = [v if isinstance(v, str) else str(v) for v in self.network_alias]

        if self.no_hosts is not None and not isinstance(self.no_hosts, Bool):
            self.no_hosts = Bool(self.no_hosts)

        if self.pid is not None and not isinstance(self.pid, str):
            self.pid = str(self.pid)

        if self.pod_id_file is not None and not isinstance(self.pod_id_file, str):
            self.pod_id_file = str(self.pod_id_file)

        if not isinstance(self.publish, list):
            self.publish = [self.publish] if self.publish is not None else []
        self.publish = [v if isinstance(v, str) else str(v) for v in self.publish]

        if self.recreate is not None and not isinstance(self.recreate, Bool):
            self.recreate = Bool(self.recreate)

        if self.share is not None and not isinstance(self.share, str):
            self.share = str(self.share)

        if self.state is not None and not isinstance(self.state, ContainerStateEnum):
            self.state = ContainerStateEnum(self.state)

        if self.subgidname is not None and not isinstance(self.subgidname, str):
            self.subgidname = str(self.subgidname)

        if self.subuidname is not None and not isinstance(self.subuidname, str):
            self.subuidname = str(self.subuidname)

        if not isinstance(self.uidmap, list):
            self.uidmap = [self.uidmap] if self.uidmap is not None else []
        self.uidmap = [v if isinstance(v, str) else str(v) for v in self.uidmap]

        if self.userns is not None and not isinstance(self.userns, str):
            self.userns = str(self.userns)

        if not isinstance(self.volume, list):
            self.volume = [self.volume] if self.volume is not None else []
        self.volume = [v if isinstance(v, str) else str(v) for v in self.volume]

        super().__post_init__(**kwargs)


@dataclass
class PodmanSave(ClosedSoftwareModule):
    """
    Saves podman image to tar file
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanSave
    class_class_curie: ClassVar[str] = "containers:PodmanSave"
    class_name: ClassVar[str] = "PodmanSave"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanSave

    dest: str = None
    image: str = None
    compress: Optional[Union[bool, Bool]] = None
    executable: Optional[str] = "podman"
    force: Optional[Union[bool, Bool]] = False
    format: Optional[Union[str, "ContainerSaveFormatEnum"]] = None
    multi_image_archive: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.dest):
            self.MissingRequiredField("dest")
        if not isinstance(self.dest, str):
            self.dest = str(self.dest)

        if self._is_empty(self.image):
            self.MissingRequiredField("image")
        if not isinstance(self.image, str):
            self.image = str(self.image)

        if self.compress is not None and not isinstance(self.compress, Bool):
            self.compress = Bool(self.compress)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if self.force is not None and not isinstance(self.force, Bool):
            self.force = Bool(self.force)

        if self.format is not None and not isinstance(self.format, ContainerSaveFormatEnum):
            self.format = ContainerSaveFormatEnum(self.format)

        if self.multi_image_archive is not None and not isinstance(self.multi_image_archive, Bool):
            self.multi_image_archive = Bool(self.multi_image_archive)

        super().__post_init__(**kwargs)


@dataclass
class PodmanSecret(ClosedSoftwareModule):
    """
    Manage Podman secrets
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanSecret
    class_class_curie: ClassVar[str] = "containers:PodmanSecret"
    class_name: ClassVar[str] = "PodmanSecret"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanSecret

    name: Union[str, LabelType] = None
    data: Optional[str] = None
    driver: Optional[str] = None
    driver_opts: Optional[Union[dict, "MetaObject"]] = None
    executable: Optional[str] = "podman"
    force: Optional[Union[bool, Bool]] = False
    skip_existing: Optional[Union[bool, Bool]] = False
    state: Optional[str] = "present"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.data is not None and not isinstance(self.data, str):
            self.data = str(self.data)

        if self.driver is not None and not isinstance(self.driver, str):
            self.driver = str(self.driver)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if self.force is not None and not isinstance(self.force, Bool):
            self.force = Bool(self.force)

        if self.skip_existing is not None and not isinstance(self.skip_existing, Bool):
            self.skip_existing = Bool(self.skip_existing)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        super().__post_init__(**kwargs)


@dataclass
class PodmanTag(ClosedSoftwareModule):
    """
    Add an additional name to a local image
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanTag
    class_class_curie: ClassVar[str] = "containers:PodmanTag"
    class_name: ClassVar[str] = "PodmanTag"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanTag

    image: str = None
    target_names: Union[str, List[str]] = None
    executable: Optional[str] = "podman"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.image):
            self.MissingRequiredField("image")
        if not isinstance(self.image, str):
            self.image = str(self.image)

        if self._is_empty(self.target_names):
            self.MissingRequiredField("target_names")
        if not isinstance(self.target_names, list):
            self.target_names = [self.target_names] if self.target_names is not None else []
        self.target_names = [v if isinstance(v, str) else str(v) for v in self.target_names]

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        super().__post_init__(**kwargs)


@dataclass
class PodmanVolume(ClosedSoftwareModule):
    """
    Manage Podman Volumes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.PodmanVolume
    class_class_curie: ClassVar[str] = "containers:PodmanVolume"
    class_name: ClassVar[str] = "PodmanVolume"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.PodmanVolume

    name: Union[str, LabelType] = None
    debug: Optional[Union[bool, Bool]] = False
    driver: Optional[str] = None
    executable: Optional[str] = "podman"
    label: Optional[Union[dict, "MetaObject"]] = None
    options: Optional[Union[str, List[str]]] = empty_list()
    recreate: Optional[Union[bool, Bool]] = False
    state: Optional[str] = "present"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.debug is not None and not isinstance(self.debug, Bool):
            self.debug = Bool(self.debug)

        if self.driver is not None and not isinstance(self.driver, str):
            self.driver = str(self.driver)

        if self.executable is not None and not isinstance(self.executable, str):
            self.executable = str(self.executable)

        if not isinstance(self.options, list):
            self.options = [self.options] if self.options is not None else []
        self.options = [v if isinstance(v, str) else str(v) for v in self.options]

        if self.recreate is not None and not isinstance(self.recreate, Bool):
            self.recreate = Bool(self.recreate)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        super().__post_init__(**kwargs)


MetaObject = Any

class OntologyClass(YAMLRoot):
    """
    A concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a ucs compatible KG can be
    considered both instances of ucs classes, and OWL classes in their own right. In general you should not need to
    use this class directly. Instead, use the appropriate ucs class, i.e. cso:ComputationalProcess
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.OntologyClass
    class_class_curie: ClassVar[str] = "ucs-core:OntologyClass"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.OntologyClass


class Annotation(YAMLRoot):
    """
    Model root class for entity annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO-CORE.Annotation
    class_class_curie: ClassVar[str] = "uco-core:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Annotation


@dataclass
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.QuantityValue
    class_class_curie: ClassVar[str] = "ucs-core:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.QuantityValue

    hasUnit: Optional[Union[str, Unit]] = None
    hasNumericValue: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hasUnit is not None and not isinstance(self.hasUnit, Unit):
            self.hasUnit = Unit(self.hasUnit)

        if self.hasNumericValue is not None and not isinstance(self.hasNumericValue, float):
            self.hasNumericValue = float(self.hasNumericValue)

        super().__post_init__(**kwargs)


@dataclass
class Attribute(Annotation):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Attribute
    class_class_curie: ClassVar[str] = "ucs-core:Attribute"
    class_name: ClassVar[str] = "Attribute"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Attribute

    hasAttributeType: Union[dict, OntologyClass] = None
    name: Optional[Union[str, LabelType]] = None
    hasQuantitativeValue: Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]] = empty_list()
    hasQualitativeValue: Optional[Union[str, NamedThingId]] = None
    iri: Optional[Union[str, IriType]] = None
    src: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.hasAttributeType):
            self.MissingRequiredField("hasAttributeType")
        if not isinstance(self.hasAttributeType, OntologyClass):
            self.hasAttributeType = OntologyClass()

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.hasQuantitativeValue, list):
            self.hasQuantitativeValue = [self.hasQuantitativeValue] if self.hasQuantitativeValue is not None else []
        self.hasQuantitativeValue = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.hasQuantitativeValue]

        if self.hasQualitativeValue is not None and not isinstance(self.hasQualitativeValue, NamedThingId):
            self.hasQualitativeValue = NamedThingId(self.hasQualitativeValue)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if self.src is not None and not isinstance(self.src, str):
            self.src = str(self.src)

        super().__post_init__(**kwargs)


@dataclass
class Entity(YAMLRoot):
    """
    Root Universal Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Entity
    class_class_curie: ClassVar[str] = "ucs-core:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Entity

    id: Union[str, EntityId] = None
    iri: Optional[Union[str, IriType]] = None
    category: Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]] = empty_list()
    type: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    hasAttribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        self._normalize_inlined_as_dict(slot_name="hasAttribute", slot_type=Attribute, key_name="hasAttributeType", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.NamedThing

    id: Union[str, NamedThingId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    providedBy: Optional[Union[str, List[str]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if not isinstance(self.providedBy, list):
            self.providedBy = [self.providedBy] if self.providedBy is not None else []
        self.providedBy = [v if isinstance(v, str) else str(v) for v in self.providedBy]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class ThingWithTaxon(YAMLRoot):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual entities,
    their products, and other operational entities and processes.
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCS-CORE.ThingWithTaxon
    class_class_curie: ClassVar[str] = "ucs-core:ThingWithTaxon"
    class_name: ClassVar[str] = "ThingWithTaxon"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.ThingWithTaxon

    inTaxon: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.inTaxon, list):
            self.inTaxon = [self.inTaxon] if self.inTaxon is not None else []
        self.inTaxon = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.inTaxon]

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeEntity(NamedThing):
    """
    Relating to the arrangements and work that is needed to control the operation of a plan
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.AdministrativeEntity
    class_class_curie: ClassVar[str] = "ucs-core:AdministrativeEntity"
    class_name: ClassVar[str] = "AdministrativeEntity"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Agent(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Agent
    class_class_curie: ClassVar[str] = "ucs-core:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Agent

    id: Union[str, AgentId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    affiliation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    address: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation] if self.affiliation is not None else []
        self.affiliation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.affiliation]

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    A piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.InformationContentEntity
    class_class_curie: ClassVar[str] = "ucs-core:InformationContentEntity"
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    license: Optional[str] = None
    rights: Optional[str] = None
    format: Optional[str] = None
    creationDate: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.creationDate is not None and not isinstance(self.creationDate, XSDDate):
            self.creationDate = XSDDate(self.creationDate)

        super().__post_init__(**kwargs)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal
    or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or
    section highlighted by NLP). The scope is intended to be general and include information published on the web, as
    well as printed materials, either directly or in one of the Publication Csolink category subclasses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Publication
    class_class_curie: ClassVar[str] = "ucs-core:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Publication

    id: Union[str, PublicationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    authors: Optional[Union[str, List[str]]] = empty_list()
    pages: Optional[Union[str, List[str]]] = empty_list()
    summary: Optional[str] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    lcshTerms: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if not isinstance(self.pages, list):
            self.pages = [self.pages] if self.pages is not None else []
        self.pages = [v if isinstance(v, str) else str(v) for v in self.pages]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if not isinstance(self.lcshTerms, list):
            self.lcshTerms = [self.lcshTerms] if self.lcshTerms is not None else []
        self.lcshTerms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.lcshTerms]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.EvidenceType
    class_class_curie: ClassVar[str] = "ucs-core:EvidenceType"
    class_name: ClassVar[str] = "EvidenceType"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.EvidenceType

    id: Union[str, EvidenceTypeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Project(AdministrativeEntity):
    """
    Collaborative enterprise, frequently involving research or design, that is carefully planned to achieve a
    particular aim
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Project
    class_class_curie: ClassVar[str] = "ucs-core:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Project

    id: Union[str, ProjectId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OpenContainerInitiative(Project):
    """
    An open governance structure for express purpose of creating open industry standards around container formats and
    runtime.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.OpenContainerInitiative
    class_class_curie: ClassVar[str] = "containers:OpenContainerInitiative"
    class_name: ClassVar[str] = "OpenContainerInitiative"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.OpenContainerInitiative

    id: Union[str, OpenContainerInitiativeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class LinuxContainersProject(Project):
    """
    Linux Containers is umbrella project for LXD, LXC, LXCFS and distrobuilder.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONTAINERS.LinuxContainersProject
    class_class_curie: ClassVar[str] = "containers:LinuxContainersProject"
    class_name: ClassVar[str] = "LinuxContainersProject"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.LinuxContainersProject

    id: Union[str, LinuxContainersProjectId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class System(NamedThing):
    """
    An entity that intends to perform some functions, interacting with other systems. Relative to a given system, the
    entities with which it interacts, are considered its environment. A system is structurally composed of a set of
    components bound together.
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCS-CORE.System
    class_class_curie: ClassVar[str] = "ucs-core:System"
    class_name: ClassVar[str] = "System"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.System

    id: Union[str, SystemId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    inTaxon: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemId):
            self.id = SystemId(self.id)

        if not isinstance(self.inTaxon, list):
            self.inTaxon = [self.inTaxon] if self.inTaxon is not None else []
        self.inTaxon = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.inTaxon]

        super().__post_init__(**kwargs)


@dataclass
class SoftwareOrDevice(System):
    """
    Either software or hardware
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCS-CORE.SoftwareOrDevice
    class_class_curie: ClassVar[str] = "ucs-core:SoftwareOrDevice"
    class_name: ClassVar[str] = "SoftwareOrDevice"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.SoftwareOrDevice

    id: Union[str, SoftwareOrDeviceId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Software(SoftwareOrDevice):
    """
    A set of instructions in a computer programming language that can be executed by a computer, possibly after
    compilation into another programming language. The term Software includes ComputerPrograms (free-standing
    software), object methods, subroutines and software packages.
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCO-CORE.Software
    class_class_curie: ClassVar[str] = "uco-core:Software"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Software

    id: Union[str, SoftwareId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareId):
            self.id = SoftwareId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Container(Software):
    """
    Software that emulates a whole computer by means of an isolated user-space environment running on top of the
    operating system's kernel.
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CONTAINERS.Container
    class_class_curie: ClassVar[str] = "containers:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Container

    id: Union[str, ContainerId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContainerId):
            self.id = ContainerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Lxc(Software):
    """
    Operating system-level virtualization for Linux
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CONTAINERS.Lxc
    class_class_curie: ClassVar[str] = "containers:Lxc"
    class_name: ClassVar[str] = "Lxc"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Lxc

    id: Union[str, LxcId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LxcId):
            self.id = LxcId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class LxcFs(Software):
    """
    LXCFS is a simple userspace filesystem designed to work around some current limitations of the Linux kernel.
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CONTAINERS.LxcFs
    class_class_curie: ClassVar[str] = "containers:LxcFs"
    class_name: ClassVar[str] = "LxcFs"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.LxcFs

    id: Union[str, LxcFsId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LxcFsId):
            self.id = LxcFsId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Lxd(Software):
    """
    Lxd is a system container and virtual machine manager for Linux OS
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CONTAINERS.Lxd
    class_class_curie: ClassVar[str] = "containers:Lxd"
    class_name: ClassVar[str] = "Lxd"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Lxd

    id: Union[str, LxdId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LxdId):
            self.id = LxdId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OciContainer(Container):
    """
    Open Container Initiative (OCI) compliant containers
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CONTAINERS.OciContainer
    class_class_curie: ClassVar[str] = "containers:OciContainer"
    class_name: ClassVar[str] = "OciContainer"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.OciContainer

    id: Union[str, OciContainerId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Podman(Software):
    """
    daemonless OCI-compliant container runtime
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CONTAINERS.Podman
    class_class_curie: ClassVar[str] = "containers:Podman"
    class_name: ClassVar[str] = "Podman"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Podman

    id: Union[str, PodmanId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Containerd(Software):
    """
    Container runtime
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CONTAINERS.Containerd
    class_class_curie: ClassVar[str] = "containers:Containerd"
    class_name: ClassVar[str] = "Containerd"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Containerd

    id: Union[str, ContainerdId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContainerdId):
            self.id = ContainerdId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Docker(Software):
    """
    open-source software for deploying containerized applications
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CONTAINERS.Docker
    class_class_curie: ClassVar[str] = "containers:Docker"
    class_name: ClassVar[str] = "Docker"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Docker

    id: Union[str, DockerId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DockerId):
            self.id = DockerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Kubernetes(Software):
    """
    software to manage containers on a server-cluster
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CONTAINERS.Kubernetes
    class_class_curie: ClassVar[str] = "containers:Kubernetes"
    class_name: ClassVar[str] = "Kubernetes"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Kubernetes

    id: Union[str, KubernetesId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KubernetesId):
            self.id = KubernetesId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Hardware(SoftwareOrDevice):
    """
    physical components of a computer
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Hardware
    class_class_curie: ClassVar[str] = "ucs-core:Hardware"
    class_name: ClassVar[str] = "Hardware"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Hardware

    id: Union[str, HardwareId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HardwareId):
            self.id = HardwareId(self.id)

        super().__post_init__(**kwargs)


class OpenSource(YAMLRoot):
    """
    Philosophy about free redistribution and access to a product
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.OpenSource
    class_class_curie: ClassVar[str] = "ucs-core:OpenSource"
    class_name: ClassVar[str] = "OpenSource"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.OpenSource


@dataclass
class OperatingSystem(Software):
    """
    An operating system (OS) is system software that manages computer hardware, software resources, and provides
    common services for computer programs.
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCO-OBSERVABLE.OperatingSystem
    class_class_curie: ClassVar[str] = "uco-observable:OperatingSystem"
    class_name: ClassVar[str] = "OperatingSystem"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.OperatingSystem

    id: Union[str, OperatingSystemId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperatingSystemId):
            self.id = OperatingSystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Solaris(OperatingSystem):
    """
    Unix operating system originally developed by Sun Microsystems
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Solaris
    class_class_curie: ClassVar[str] = "ucs-core:Solaris"
    class_name: ClassVar[str] = "Solaris"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Solaris

    id: Union[str, SolarisId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SolarisId):
            self.id = SolarisId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Linux(OperatingSystem):
    """
    family of Unix-like operating systems using Linux kernel and open source
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Linux
    class_class_curie: ClassVar[str] = "ucs-core:Linux"
    class_name: ClassVar[str] = "Linux"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Linux

    id: Union[str, LinuxId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LinuxId):
            self.id = LinuxId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Windows(OperatingSystem):
    """
    family of computer operating systems developed by Microsoft
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Windows
    class_class_curie: ClassVar[str] = "ucs-core:Windows"
    class_name: ClassVar[str] = "Windows"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Windows

    id: Union[str, WindowsId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsId):
            self.id = WindowsId(self.id)

        super().__post_init__(**kwargs)


class Virtualization(YAMLRoot):
    """
    computing technique for setting up virtual versions of operating systems or computer resources
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Virtualization
    class_class_curie: ClassVar[str] = "ucs-core:Virtualization"
    class_name: ClassVar[str] = "Virtualization"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Virtualization


@dataclass
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS-CORE.Association
    class_class_curie: ClassVar[str] = "ucs-core:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = CONTAINERS.Association

    id: Union[str, AssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    negated: Optional[Union[bool, Bool]] = None
    qualifiers: Optional[Union[Union[dict, OntologyClass], List[Union[dict, OntologyClass]]]] = empty_list()
    publications: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    hasEvidence: Optional[Union[Union[str, EvidenceTypeId], List[Union[str, EvidenceTypeId]]]] = empty_list()
    type: Optional[str] = None
    category: Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, OntologyClass) else OntologyClass(**as_dict(v)) for v in self.qualifiers]

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.publications]

        if not isinstance(self.hasEvidence, list):
            self.hasEvidence = [self.hasEvidence] if self.hasEvidence is not None else []
        self.hasEvidence = [v if isinstance(v, EvidenceTypeId) else EvidenceTypeId(v) for v in self.hasEvidence]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        super().__post_init__(**kwargs)


# Enumerations
class ContainerRestartPolicyEnum(EnumDefinitionImpl):
    """
    Restart policy after exit
    """
    no = PermissibleValue(text="no")
    always = PermissibleValue(text="always")

    _defn = EnumDefinition(
        name="ContainerRestartPolicyEnum",
        description="Restart policy after exit",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "on-success",
                PermissibleValue(text="on-success") )
        setattr(cls, "on-failure",
                PermissibleValue(text="on-failure") )
        setattr(cls, "on-abnormal",
                PermissibleValue(text="on-abnormal") )
        setattr(cls, "on-watchdog",
                PermissibleValue(text="on-watchdog") )
        setattr(cls, "on-abort",
                PermissibleValue(text="on-abort") )

class ContainerStateEnum(EnumDefinitionImpl):
    """
    Valid values for Container state
    """
    absent = PermissibleValue(text="absent",
                                   description="A container matching the specified name will be stopped and removed.")
    present = PermissibleValue(text="present",
                                     description="Asserts the existence of a container matching the name and any provided configuration parameters.")
    started = PermissibleValue(text="started",
                                     description="Asserts there is a running container matching the name and any provided configuration.")
    stopped = PermissibleValue(text="stopped",
                                     description="Asserts that the container is first present, and then if the container is running moves it to a stopped state.")
    created = PermissibleValue(text="created",
                                     description="Asserts that the container exists with given configuration.")

    _defn = EnumDefinition(
        name="ContainerStateEnum",
        description="Valid values for Container state",
    )

class ContainerImageStateEnum(EnumDefinitionImpl):
    """
    Valid values for Container Image state
    """
    absent = PermissibleValue(text="absent")
    present = PermissibleValue(text="present")
    build = PermissibleValue(text="build")

    _defn = EnumDefinition(
        name="ContainerImageStateEnum",
        description="Valid values for Container Image state",
    )

class CgroupsEnum(EnumDefinitionImpl):
    """
    Use cgroups or not
    """
    enabled = PermissibleValue(text="enabled")
    disabled = PermissibleValue(text="disabled")

    _defn = EnumDefinition(
        name="CgroupsEnum",
        description="Use cgroups or not",
    )

class ContainerImageVolumeEnum(EnumDefinitionImpl):
    """
    Builtin image volume handling
    """
    bind = PermissibleValue(text="bind")
    tmpfs = PermissibleValue(text="tmpfs")
    ignore = PermissibleValue(text="ignore")

    _defn = EnumDefinition(
        name="ContainerImageVolumeEnum",
        description="Builtin image volume handling",
    )

class ContainerLogDriverEnum(EnumDefinitionImpl):
    """
    Logging driver.
    """
    journald = PermissibleValue(text="journald")

    _defn = EnumDefinition(
        name="ContainerLogDriverEnum",
        description="Logging driver.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "k8s-file",
                PermissibleValue(text="k8s-file") )
        setattr(cls, "json-file",
                PermissibleValue(text="json-file") )

class ContainerSaveFormatEnum(EnumDefinitionImpl):
    """
    Image save format
    """
    _defn = EnumDefinition(
        name="ContainerSaveFormatEnum",
        description="Image save format",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "docker-archive",
                PermissibleValue(text="docker-archive") )
        setattr(cls, "oci-archive",
                PermissibleValue(text="oci-archive") )
        setattr(cls, "oci-dir",
                PermissibleValue(text="oci-dir") )
        setattr(cls, "docker-dir",
                PermissibleValue(text="docker-dir") )

class ContainerLogLevelEnum(EnumDefinitionImpl):
    """
    Logging level.
    """
    debug = PermissibleValue(text="debug")
    info = PermissibleValue(text="info")
    warn = PermissibleValue(text="warn")
    error = PermissibleValue(text="error")
    fatal = PermissibleValue(text="fatal")
    panic = PermissibleValue(text="panic")

    _defn = EnumDefinition(
        name="ContainerLogLevelEnum",
        description="Logging level.",
    )

class ContainerImageFormatEnum(EnumDefinitionImpl):
    """
    Container format
    """
    oci = PermissibleValue(text="oci")
    v2s1 = PermissibleValue(text="v2s1")
    v2s2 = PermissibleValue(text="v2s2")

    _defn = EnumDefinition(
        name="ContainerImageFormatEnum",
        description="Container format",
    )

class ContainerImagePushTransportEnum(EnumDefinitionImpl):
    """
    Transport to use when pushing in image.
    """
    dir = PermissibleValue(text="dir")
    ostree = PermissibleValue(text="ostree")

    _defn = EnumDefinition(
        name="ContainerImagePushTransportEnum",
        description="Transport to use when pushing in image.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "docker-archive",
                PermissibleValue(text="docker-archive") )
        setattr(cls, "docker-daemon",
                PermissibleValue(text="docker-daemon") )
        setattr(cls, "oci-archive",
                PermissibleValue(text="oci-archive") )

class ContainerNetworkStateEnum(EnumDefinitionImpl):

    present = PermissibleValue(text="present")
    absent = PermissibleValue(text="absent")

    _defn = EnumDefinition(
        name="ContainerNetworkStateEnum",
    )

# Slots
class slots:
    pass

slots.blkio_weight = Slot(uri=CONTAINERS.blkio_weight, name="blkio_weight", curie=CONTAINERS.curie('blkio_weight'),
                   model_uri=CONTAINERS.blkio_weight, domain=None, range=Optional[int])

slots.blkio_weight_device = Slot(uri=CONTAINERS.blkio_weight_device, name="blkio_weight_device", curie=CONTAINERS.curie('blkio_weight_device'),
                   model_uri=CONTAINERS.blkio_weight_device, domain=None, range=Optional[Union[str, List[str]]])

slots.cap_add = Slot(uri=CONTAINERS.cap_add, name="cap_add", curie=CONTAINERS.curie('cap_add'),
                   model_uri=CONTAINERS.cap_add, domain=None, range=Optional[Union[str, List[str]]])

slots.cap_drop = Slot(uri=CONTAINERS.cap_drop, name="cap_drop", curie=CONTAINERS.curie('cap_drop'),
                   model_uri=CONTAINERS.cap_drop, domain=None, range=Optional[Union[str, List[str]]])

slots.cgroup_parent = Slot(uri=CONTAINERS.cgroup_parent, name="cgroup_parent", curie=CONTAINERS.curie('cgroup_parent'),
                   model_uri=CONTAINERS.cgroup_parent, domain=None, range=Optional[str])

slots.cgroupns = Slot(uri=CONTAINERS.cgroupns, name="cgroupns", curie=CONTAINERS.curie('cgroupns'),
                   model_uri=CONTAINERS.cgroupns, domain=None, range=Optional[str])

slots.cidfile = Slot(uri=CONTAINERS.cidfile, name="cidfile", curie=CONTAINERS.curie('cidfile'),
                   model_uri=CONTAINERS.cidfile, domain=None, range=Optional[str])

slots.conmon_pidfile = Slot(uri=CONTAINERS.conmon_pidfile, name="conmon_pidfile", curie=CONTAINERS.curie('conmon_pidfile'),
                   model_uri=CONTAINERS.conmon_pidfile, domain=None, range=Optional[str])

slots.cpu_period = Slot(uri=CONTAINERS.cpu_period, name="cpu_period", curie=CONTAINERS.curie('cpu_period'),
                   model_uri=CONTAINERS.cpu_period, domain=None, range=Optional[int])

slots.cpu_rt_period = Slot(uri=CONTAINERS.cpu_rt_period, name="cpu_rt_period", curie=CONTAINERS.curie('cpu_rt_period'),
                   model_uri=CONTAINERS.cpu_rt_period, domain=None, range=Optional[int])

slots.cpu_rt_runtime = Slot(uri=CONTAINERS.cpu_rt_runtime, name="cpu_rt_runtime", curie=CONTAINERS.curie('cpu_rt_runtime'),
                   model_uri=CONTAINERS.cpu_rt_runtime, domain=None, range=Optional[int])

slots.cpu_shares = Slot(uri=CONTAINERS.cpu_shares, name="cpu_shares", curie=CONTAINERS.curie('cpu_shares'),
                   model_uri=CONTAINERS.cpu_shares, domain=None, range=Optional[int])

slots.cpuset_cpus = Slot(uri=CONTAINERS.cpuset_cpus, name="cpuset_cpus", curie=CONTAINERS.curie('cpuset_cpus'),
                   model_uri=CONTAINERS.cpuset_cpus, domain=None, range=Optional[str])

slots.cpuset_mems = Slot(uri=CONTAINERS.cpuset_mems, name="cpuset_mems", curie=CONTAINERS.curie('cpuset_mems'),
                   model_uri=CONTAINERS.cpuset_mems, domain=None, range=Optional[str])

slots.detach = Slot(uri=CONTAINERS.detach, name="detach", curie=CONTAINERS.curie('detach'),
                   model_uri=CONTAINERS.detach, domain=None, range=Optional[str])

slots.detach_keys = Slot(uri=CONTAINERS.detach_keys, name="detach_keys", curie=CONTAINERS.curie('detach_keys'),
                   model_uri=CONTAINERS.detach_keys, domain=None, range=Optional[str])

slots.device_read_bps = Slot(uri=CONTAINERS.device_read_bps, name="device_read_bps", curie=CONTAINERS.curie('device_read_bps'),
                   model_uri=CONTAINERS.device_read_bps, domain=None, range=Optional[str])

slots.device_read_iops = Slot(uri=CONTAINERS.device_read_iops, name="device_read_iops", curie=CONTAINERS.curie('device_read_iops'),
                   model_uri=CONTAINERS.device_read_iops, domain=None, range=Optional[str])

slots.device_write_bps = Slot(uri=CONTAINERS.device_write_bps, name="device_write_bps", curie=CONTAINERS.curie('device_write_bps'),
                   model_uri=CONTAINERS.device_write_bps, domain=None, range=Optional[str])

slots.device_write_iops = Slot(uri=CONTAINERS.device_write_iops, name="device_write_iops", curie=CONTAINERS.curie('device_write_iops'),
                   model_uri=CONTAINERS.device_write_iops, domain=None, range=Optional[str])

slots.entrypoint = Slot(uri=CONTAINERS.entrypoint, name="entrypoint", curie=CONTAINERS.curie('entrypoint'),
                   model_uri=CONTAINERS.entrypoint, domain=None, range=Optional[str])

slots.env_host = Slot(uri=CONTAINERS.env_host, name="env_host", curie=CONTAINERS.curie('env_host'),
                   model_uri=CONTAINERS.env_host, domain=None, range=Optional[str])

slots.force_restart = Slot(uri=CONTAINERS.force_restart, name="force_restart", curie=CONTAINERS.curie('force_restart'),
                   model_uri=CONTAINERS.force_restart, domain=None, range=Optional[Union[bool, Bool]])

slots.generate_systemd = Slot(uri=CONTAINERS.generate_systemd, name="generate_systemd", curie=CONTAINERS.curie('generate_systemd'),
                   model_uri=CONTAINERS.generate_systemd, domain=None, range=Optional[Union[dict, MetaObject]])

slots.no_header = Slot(uri=CONTAINERS.no_header, name="no_header", curie=CONTAINERS.curie('no_header'),
                   model_uri=CONTAINERS.no_header, domain=None, range=Optional[Union[bool, Bool]])

slots.use_names = Slot(uri=CONTAINERS.use_names, name="use_names", curie=CONTAINERS.curie('use_names'),
                   model_uri=CONTAINERS.use_names, domain=None, range=Optional[Union[bool, Bool]])

slots.container_prefix = Slot(uri=CONTAINERS.container_prefix, name="container_prefix", curie=CONTAINERS.curie('container_prefix'),
                   model_uri=CONTAINERS.container_prefix, domain=None, range=Optional[str])

slots.containers = Slot(uri=CONTAINERS.containers, name="containers", curie=CONTAINERS.curie('containers'),
                   model_uri=CONTAINERS.containers, domain=None, range=Optional[str])

slots.pod_prefix = Slot(uri=CONTAINERS.pod_prefix, name="pod_prefix", curie=CONTAINERS.curie('pod_prefix'),
                   model_uri=CONTAINERS.pod_prefix, domain=None, range=Optional[str])

slots.wants = Slot(uri=CONTAINERS.wants, name="wants", curie=CONTAINERS.curie('wants'),
                   model_uri=CONTAINERS.wants, domain=None, range=Optional[Union[str, List[str]]])

slots.gidmap = Slot(uri=CONTAINERS.gidmap, name="gidmap", curie=CONTAINERS.curie('gidmap'),
                   model_uri=CONTAINERS.gidmap, domain=None, range=Optional[Union[str, List[str]]])

slots.group_add = Slot(uri=CONTAINERS.group_add, name="group_add", curie=CONTAINERS.curie('group_add'),
                   model_uri=CONTAINERS.group_add, domain=None, range=Optional[Union[str, List[str]]])

slots.healthcheck_start_period = Slot(uri=CONTAINERS.healthcheck_start_period, name="healthcheck_start_period", curie=CONTAINERS.curie('healthcheck_start_period'),
                   model_uri=CONTAINERS.healthcheck_start_period, domain=None, range=Optional[str])

slots.hooks_dir = Slot(uri=CONTAINERS.hooks_dir, name="hooks_dir", curie=CONTAINERS.curie('hooks_dir'),
                   model_uri=CONTAINERS.hooks_dir, domain=None, range=Optional[str])

slots.image_volume = Slot(uri=CONTAINERS.image_volume, name="image_volume", curie=CONTAINERS.curie('image_volume'),
                   model_uri=CONTAINERS.image_volume, domain=None, range=Optional[str])

slots.multi_image_archive = Slot(uri=CONTAINERS.multi_image_archive, name="multi_image_archive", curie=CONTAINERS.curie('multi_image_archive'),
                   model_uri=CONTAINERS.multi_image_archive, domain=None, range=Optional[Union[bool, Bool]])

slots.target_names = Slot(uri=CONTAINERS.target_names, name="target_names", curie=CONTAINERS.curie('target_names'),
                   model_uri=CONTAINERS.target_names, domain=None, range=Optional[str])

slots.skip_existing = Slot(uri=CONTAINERS.skip_existing, name="skip_existing", curie=CONTAINERS.curie('skip_existing'),
                   model_uri=CONTAINERS.skip_existing, domain=None, range=Optional[Union[bool, Bool]])

slots.image_strict = Slot(uri=CONTAINERS.image_strict, name="image_strict", curie=CONTAINERS.curie('image_strict'),
                   model_uri=CONTAINERS.image_strict, domain=None, range=Optional[Union[bool, Bool]])

slots.init_path = Slot(uri=CONTAINERS.init_path, name="init_path", curie=CONTAINERS.curie('init_path'),
                   model_uri=CONTAINERS.init_path, domain=None, range=Optional[str])

slots.ipc = Slot(uri=CONTAINERS.ipc, name="ipc", curie=CONTAINERS.curie('ipc'),
                   model_uri=CONTAINERS.ipc, domain=None, range=Optional[str])

slots.kernel_memory = Slot(uri=CONTAINERS.kernel_memory, name="kernel_memory", curie=CONTAINERS.curie('kernel_memory'),
                   model_uri=CONTAINERS.kernel_memory, domain=None, range=Optional[str])

slots.label_file = Slot(uri=CONTAINERS.label_file, name="label_file", curie=CONTAINERS.curie('label_file'),
                   model_uri=CONTAINERS.label_file, domain=None, range=Optional[str])

slots.log_opt = Slot(uri=CONTAINERS.log_opt, name="log_opt", curie=CONTAINERS.curie('log_opt'),
                   model_uri=CONTAINERS.log_opt, domain=None, range=Optional[Union[dict, MetaObject]])

slots.memory_reservation = Slot(uri=CONTAINERS.memory_reservation, name="memory_reservation", curie=CONTAINERS.curie('memory_reservation'),
                   model_uri=CONTAINERS.memory_reservation, domain=None, range=Optional[str])

slots.memory_swap = Slot(uri=CONTAINERS.memory_swap, name="memory_swap", curie=CONTAINERS.curie('memory_swap'),
                   model_uri=CONTAINERS.memory_swap, domain=None, range=Optional[str])

slots.memory_swappiness = Slot(uri=CONTAINERS.memory_swappiness, name="memory_swappiness", curie=CONTAINERS.curie('memory_swappiness'),
                   model_uri=CONTAINERS.memory_swappiness, domain=None, range=Optional[int])

slots.network_aliases = Slot(uri=CONTAINERS.network_aliases, name="network_aliases", curie=CONTAINERS.curie('network_aliases'),
                   model_uri=CONTAINERS.network_aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.network_alias = Slot(uri=CONTAINERS.network_alias, name="network_alias", curie=CONTAINERS.curie('network_alias'),
                   model_uri=CONTAINERS.network_alias, domain=None, range=Optional[str])

slots.no_hosts = Slot(uri=CONTAINERS.no_hosts, name="no_hosts", curie=CONTAINERS.curie('no_hosts'),
                   model_uri=CONTAINERS.no_hosts, domain=None, range=Optional[Union[bool, Bool]])

slots.oom_kill_disable = Slot(uri=CONTAINERS.oom_kill_disable, name="oom_kill_disable", curie=CONTAINERS.curie('oom_kill_disable'),
                   model_uri=CONTAINERS.oom_kill_disable, domain=None, range=Optional[Union[bool, Bool]])

slots.oom_score_adj = Slot(uri=CONTAINERS.oom_score_adj, name="oom_score_adj", curie=CONTAINERS.curie('oom_score_adj'),
                   model_uri=CONTAINERS.oom_score_adj, domain=None, range=Optional[int])

slots.pids_limit = Slot(uri=CONTAINERS.pids_limit, name="pids_limit", curie=CONTAINERS.curie('pids_limit'),
                   model_uri=CONTAINERS.pids_limit, domain=None, range=Optional[int])

slots.pod = Slot(uri=CONTAINERS.pod, name="pod", curie=CONTAINERS.curie('pod'),
                   model_uri=CONTAINERS.pod, domain=None, range=Optional[str])

slots.expose = Slot(uri=CONTAINERS.expose, name="expose", curie=CONTAINERS.curie('expose'),
                   model_uri=CONTAINERS.expose, domain=None, range=Optional[str])

slots.publish_all = Slot(uri=CONTAINERS.publish_all, name="publish_all", curie=CONTAINERS.curie('publish_all'),
                   model_uri=CONTAINERS.publish_all, domain=None, range=Optional[Union[bool, Bool]])

slots.read_only_tmpfs = Slot(uri=CONTAINERS.read_only_tmpfs, name="read_only_tmpfs", curie=CONTAINERS.curie('read_only_tmpfs'),
                   model_uri=CONTAINERS.read_only_tmpfs, domain=None, range=Optional[Union[bool, Bool]])

slots.requires = Slot(uri=CONTAINERS.requires, name="requires", curie=CONTAINERS.curie('requires'),
                   model_uri=CONTAINERS.requires, domain=None, range=Optional[Union[str, List[str]]])

slots.restart_policy = Slot(uri=CONTAINERS.restart_policy, name="restart_policy", curie=CONTAINERS.curie('restart_policy'),
                   model_uri=CONTAINERS.restart_policy, domain=None, range=Optional[str])

slots.restart_sec = Slot(uri=CONTAINERS.restart_sec, name="restart_sec", curie=CONTAINERS.curie('restart_sec'),
                   model_uri=CONTAINERS.restart_sec, domain=None, range=Optional[str])

slots.sdnotify = Slot(uri=CONTAINERS.sdnotify, name="sdnotify", curie=CONTAINERS.curie('sdnotify'),
                   model_uri=CONTAINERS.sdnotify, domain=None, range=Optional[str])

slots.security_opt = Slot(uri=CONTAINERS.security_opt, name="security_opt", curie=CONTAINERS.curie('security_opt'),
                   model_uri=CONTAINERS.security_opt, domain=None, range=Optional[Union[str, List[str]]])

slots.shm_size = Slot(uri=CONTAINERS.shm_size, name="shm_size", curie=CONTAINERS.curie('shm_size'),
                   model_uri=CONTAINERS.shm_size, domain=None, range=Optional[str])

slots.sig_proxy = Slot(uri=CONTAINERS.sig_proxy, name="sig_proxy", curie=CONTAINERS.curie('sig_proxy'),
                   model_uri=CONTAINERS.sig_proxy, domain=None, range=Optional[str])

slots.stop_signal = Slot(uri=CONTAINERS.stop_signal, name="stop_signal", curie=CONTAINERS.curie('stop_signal'),
                   model_uri=CONTAINERS.stop_signal, domain=None, range=Optional[int])

slots.start_timeout = Slot(uri=CONTAINERS.start_timeout, name="start_timeout", curie=CONTAINERS.curie('start_timeout'),
                   model_uri=CONTAINERS.start_timeout, domain=None, range=Optional[int])

slots.stop_timeout = Slot(uri=CONTAINERS.stop_timeout, name="stop_timeout", curie=CONTAINERS.curie('stop_timeout'),
                   model_uri=CONTAINERS.stop_timeout, domain=None, range=Optional[int])

slots.subgidname = Slot(uri=CONTAINERS.subgidname, name="subgidname", curie=CONTAINERS.curie('subgidname'),
                   model_uri=CONTAINERS.subgidname, domain=None, range=Optional[str])

slots.subuidname = Slot(uri=CONTAINERS.subuidname, name="subuidname", curie=CONTAINERS.curie('subuidname'),
                   model_uri=CONTAINERS.subuidname, domain=None, range=Optional[str])

slots.uidmap = Slot(uri=CONTAINERS.uidmap, name="uidmap", curie=CONTAINERS.curie('uidmap'),
                   model_uri=CONTAINERS.uidmap, domain=None, range=Optional[str])

slots.userns = Slot(uri=CONTAINERS.userns, name="userns", curie=CONTAINERS.curie('userns'),
                   model_uri=CONTAINERS.userns, domain=None, range=Optional[str])

slots.volumes_from = Slot(uri=CONTAINERS.volumes_from, name="volumes_from", curie=CONTAINERS.curie('volumes_from'),
                   model_uri=CONTAINERS.volumes_from, domain=None, range=Optional[Union[str, List[str]]])

slots.ca_cert_dir = Slot(uri=CONTAINERS.ca_cert_dir, name="ca_cert_dir", curie=CONTAINERS.curie('ca_cert_dir'),
                   model_uri=CONTAINERS.ca_cert_dir, domain=None, range=Optional[str])

slots.extra_args = Slot(uri=CONTAINERS.extra_args, name="extra_args", curie=CONTAINERS.curie('extra_args'),
                   model_uri=CONTAINERS.extra_args, domain=None, range=Optional[str])

slots.force_rm = Slot(uri=CONTAINERS.force_rm, name="force_rm", curie=CONTAINERS.curie('force_rm'),
                   model_uri=CONTAINERS.force_rm, domain=None, range=Optional[str])

slots.pull = Slot(uri=CONTAINERS.pull, name="pull", curie=CONTAINERS.curie('pull'),
                   model_uri=CONTAINERS.pull, domain=None, range=Optional[str])

slots.push = Slot(uri=CONTAINERS.push, name="push", curie=CONTAINERS.curie('push'),
                   model_uri=CONTAINERS.push, domain=None, range=Optional[str])

slots.remove_signatures = Slot(uri=CONTAINERS.remove_signatures, name="remove_signatures", curie=CONTAINERS.curie('remove_signatures'),
                   model_uri=CONTAINERS.remove_signatures, domain=None, range=Optional[str])

slots.sign_by = Slot(uri=CONTAINERS.sign_by, name="sign_by", curie=CONTAINERS.curie('sign_by'),
                   model_uri=CONTAINERS.sign_by, domain=None, range=Optional[str])

slots.push_args = Slot(uri=CONTAINERS.push_args, name="push_args", curie=CONTAINERS.curie('push_args'),
                   model_uri=CONTAINERS.push_args, domain=None, range=Optional[str])

slots.registry = Slot(uri=CONTAINERS.registry, name="registry", curie=CONTAINERS.curie('registry'),
                   model_uri=CONTAINERS.registry, domain=None, range=Optional[str])

slots.all = Slot(uri=CONTAINERS.all, name="all", curie=CONTAINERS.curie('all'),
                   model_uri=CONTAINERS.all, domain=None, range=Optional[str])

slots.ignore_docker_credentials = Slot(uri=CONTAINERS.ignore_docker_credentials, name="ignore_docker_credentials", curie=CONTAINERS.curie('ignore_docker_credentials'),
                   model_uri=CONTAINERS.ignore_docker_credentials, domain=None, range=Optional[str])

slots.disable_dns = Slot(uri=CONTAINERS.disable_dns, name="disable_dns", curie=CONTAINERS.curie('disable_dns'),
                   model_uri=CONTAINERS.disable_dns, domain=None, range=Optional[Union[bool, Bool]])

slots.macvlan = Slot(uri=CONTAINERS.macvlan, name="macvlan", curie=CONTAINERS.curie('macvlan'),
                   model_uri=CONTAINERS.macvlan, domain=None, range=Optional[str])

slots.configmap = Slot(uri=CONTAINERS.configmap, name="configmap", curie=CONTAINERS.curie('configmap'),
                   model_uri=CONTAINERS.configmap, domain=None, range=Optional[str])

slots.kube_file = Slot(uri=CONTAINERS.kube_file, name="kube_file", curie=CONTAINERS.curie('kube_file'),
                   model_uri=CONTAINERS.kube_file, domain=None, range=Optional[str])

slots.seccomp_profile_root = Slot(uri=CONTAINERS.seccomp_profile_root, name="seccomp_profile_root", curie=CONTAINERS.curie('seccomp_profile_root'),
                   model_uri=CONTAINERS.seccomp_profile_root, domain=None, range=Optional[str])

slots.add_host = Slot(uri=CONTAINERS.add_host, name="add_host", curie=CONTAINERS.curie('add_host'),
                   model_uri=CONTAINERS.add_host, domain=None, range=Optional[str])

slots.infra_command = Slot(uri=CONTAINERS.infra_command, name="infra_command", curie=CONTAINERS.curie('infra_command'),
                   model_uri=CONTAINERS.infra_command, domain=None, range=Optional[str])

slots.infra_conmon_pidfile = Slot(uri=CONTAINERS.infra_conmon_pidfile, name="infra_conmon_pidfile", curie=CONTAINERS.curie('infra_conmon_pidfile'),
                   model_uri=CONTAINERS.infra_conmon_pidfile, domain=None, range=Optional[str])

slots.infra_name = Slot(uri=CONTAINERS.infra_name, name="infra_name", curie=CONTAINERS.curie('infra_name'),
                   model_uri=CONTAINERS.infra_name, domain=None, range=Optional[str])

slots.infra_image = Slot(uri=CONTAINERS.infra_image, name="infra_image", curie=CONTAINERS.curie('infra_image'),
                   model_uri=CONTAINERS.infra_image, domain=None, range=Optional[str])

slots.pod_id_file = Slot(uri=CONTAINERS.pod_id_file, name="pod_id_file", curie=CONTAINERS.curie('pod_id_file'),
                   model_uri=CONTAINERS.pod_id_file, domain=None, range=Optional[str])

slots.hasAttribute = Slot(uri=CORE.hasAttribute, name="hasAttribute", curie=CORE.curie('hasAttribute'),
                   model_uri=CONTAINERS.hasAttribute, domain=Entity, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.hasAttributeType = Slot(uri=CORE.hasAttributeType, name="hasAttributeType", curie=CORE.curie('hasAttributeType'),
                   model_uri=CONTAINERS.hasAttributeType, domain=Attribute, range=Union[dict, OntologyClass])

slots.hasQualitativeValue = Slot(uri=CORE.hasQualitativeValue, name="hasQualitativeValue", curie=CORE.curie('hasQualitativeValue'),
                   model_uri=CONTAINERS.hasQualitativeValue, domain=Attribute, range=Optional[Union[str, NamedThingId]])

slots.hasQuantitativeValue = Slot(uri=CORE.hasQuantitativeValue, name="hasQuantitativeValue", curie=CORE.curie('hasQuantitativeValue'),
                   model_uri=CONTAINERS.hasQuantitativeValue, domain=Attribute, range=Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]])

slots.hasNumericValue = Slot(uri=CORE.hasNumericValue, name="hasNumericValue", curie=CORE.curie('hasNumericValue'),
                   model_uri=CONTAINERS.hasNumericValue, domain=QuantityValue, range=Optional[float])

slots.hasUnit = Slot(uri=CORE.hasUnit, name="hasUnit", curie=CORE.curie('hasUnit'),
                   model_uri=CONTAINERS.hasUnit, domain=QuantityValue, range=Optional[Union[str, Unit]])

slots.nodeProperty = Slot(uri=CORE.nodeProperty, name="nodeProperty", curie=CORE.curie('nodeProperty'),
                   model_uri=CONTAINERS.nodeProperty, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=CORE.id, name="id", curie=CORE.curie('id'),
                   model_uri=CONTAINERS.id, domain=Entity, range=Union[str, EntityId])

slots.iri = Slot(uri=CORE.iri, name="iri", curie=CORE.curie('iri'),
                   model_uri=CONTAINERS.iri, domain=None, range=Optional[Union[str, IriType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=CONTAINERS.type, domain=None, range=Optional[str])

slots.category = Slot(uri=CORE.category, name="category", curie=CORE.curie('category'),
                   model_uri=CONTAINERS.category, domain=Entity, range=Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CONTAINERS.name, domain=None, range=Optional[Union[str, LabelType]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=CONTAINERS.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.xref = Slot(uri=CORE.xref, name="xref", curie=CORE.curie('xref'),
                   model_uri=CONTAINERS.xref, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.affiliation = Slot(uri=CORE.affiliation, name="affiliation", curie=CORE.curie('affiliation'),
                   model_uri=CONTAINERS.affiliation, domain=Agent, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.address = Slot(uri=UCO-IDENTITY.address, name="address", curie=UCO-IDENTITY.curie('address'),
                   model_uri=CONTAINERS.address, domain=None, range=Optional[str])

slots.creationDate = Slot(uri=UCO-OBSERVABLE.creationDate, name="creationDate", curie=UCO-OBSERVABLE.curie('creationDate'),
                   model_uri=CONTAINERS.creationDate, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.providedBy = Slot(uri=CORE.providedBy, name="providedBy", curie=CORE.curie('providedBy'),
                   model_uri=CONTAINERS.providedBy, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.inTaxon = Slot(uri=CORE.inTaxon, name="inTaxon", curie=CORE.curie('inTaxon'),
                   model_uri=CONTAINERS.inTaxon, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.taxonOf = Slot(uri=CORE.taxonOf, name="taxonOf", curie=CORE.curie('taxonOf'),
                   model_uri=CONTAINERS.taxonOf, domain=NamedThing, range=Optional[Union[Union[dict, "ThingWithTaxon"], List[Union[dict, "ThingWithTaxon"]]]])

slots.associationSlot = Slot(uri=CORE.associationSlot, name="associationSlot", curie=CORE.curie('associationSlot'),
                   model_uri=CONTAINERS.associationSlot, domain=Association, range=Optional[str])

slots.relatedTo = Slot(uri=CORE.relatedTo, name="relatedTo", curie=CORE.curie('relatedTo'),
                   model_uri=CONTAINERS.relatedTo, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.relatedToAtInstanceLevel = Slot(uri=CORE.relatedToAtInstanceLevel, name="relatedToAtInstanceLevel", curie=CORE.curie('relatedToAtInstanceLevel'),
                   model_uri=CONTAINERS.relatedToAtInstanceLevel, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.image = Slot(uri=CORE.image, name="image", curie=CORE.curie('image'),
                   model_uri=CONTAINERS.image, domain=None, range=Optional[str])

slots.etc_hosts = Slot(uri=CORE.etc_hosts, name="etc_hosts", curie=CORE.curie('etc_hosts'),
                   model_uri=CONTAINERS.etc_hosts, domain=None, range=Optional[str])

slots.container = Slot(uri=CORE.container, name="container", curie=CORE.curie('container'),
                   model_uri=CONTAINERS.container, domain=None, range=Optional[str])

slots.build = Slot(uri=CORE.build, name="build", curie=CORE.curie('build'),
                   model_uri=CONTAINERS.build, domain=None, range=Optional[str])

slots.data = Slot(uri=UCO-OBSERVABLE.data, name="data", curie=UCO-OBSERVABLE.curie('data'),
                   model_uri=CONTAINERS.data, domain=None, range=Optional[str])

slots.executable = Slot(uri=CORE.executable, name="executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.executable, domain=None, range=Optional[str])

slots.state = Slot(uri=UCO-OBSERVABLE.state, name="state", curie=UCO-OBSERVABLE.curie('state'),
                   model_uri=CONTAINERS.state, domain=Association, range=Optional[str])

slots.annotation = Slot(uri=CORE.annotation, name="annotation", curie=CORE.curie('annotation'),
                   model_uri=CONTAINERS.annotation, domain=None, range=Optional[str])

slots.authfile = Slot(uri=CORE.authfile, name="authfile", curie=CORE.curie('authfile'),
                   model_uri=CONTAINERS.authfile, domain=None, range=Optional[str])

slots.auth_file = Slot(uri=CORE.auth_file, name="auth_file", curie=CORE.curie('auth_file'),
                   model_uri=CONTAINERS.auth_file, domain=None, range=Optional[str])

slots.tag = Slot(uri=CORE.tag, name="tag", curie=CORE.curie('tag'),
                   model_uri=CONTAINERS.tag, domain=None, range=Optional[str])

slots.cgroups = Slot(uri=CORE.cgroups, name="cgroups", curie=CORE.curie('cgroups'),
                   model_uri=CONTAINERS.cgroups, domain=None, range=Optional[str])

slots.cmd_args = Slot(uri=CORE.cmd_args, name="cmd_args", curie=CORE.curie('cmd_args'),
                   model_uri=CONTAINERS.cmd_args, domain=None, range=Optional[Union[str, List[str]]])

slots.command = Slot(uri=CORE.command, name="command", curie=CORE.curie('command'),
                   model_uri=CONTAINERS.command, domain=None, range=Optional[str])

slots.cpus = Slot(uri=CORE.cpus, name="cpus", curie=CORE.curie('cpus'),
                   model_uri=CONTAINERS.cpus, domain=None, range=Optional[str])

slots.debug = Slot(uri=CORE.debug, name="debug", curie=CORE.curie('debug'),
                   model_uri=CONTAINERS.debug, domain=None, range=Optional[str])

slots.device = Slot(uri=CORE.device, name="device", curie=CORE.curie('device'),
                   model_uri=CONTAINERS.device, domain=None, range=Optional[str])

slots.dns = Slot(uri=CORE.dns, name="dns", curie=CORE.curie('dns'),
                   model_uri=CONTAINERS.dns, domain=None, range=Optional[Union[str, List[str]]])

slots.dns_option = Slot(uri=CORE.dns_option, name="dns_option", curie=CORE.curie('dns_option'),
                   model_uri=CONTAINERS.dns_option, domain=None, range=Optional[str])

slots.dns_opt = Slot(uri=CORE.dns_opt, name="dns_opt", curie=CORE.curie('dns_opt'),
                   model_uri=CONTAINERS.dns_opt, domain=None, range=Optional[str])

slots.dns_search = Slot(uri=CORE.dns_search, name="dns_search", curie=CORE.curie('dns_search'),
                   model_uri=CONTAINERS.dns_search, domain=None, range=Optional[str])

slots.env = Slot(uri=CORE.env, name="env", curie=CORE.curie('env'),
                   model_uri=CONTAINERS.env, domain=None, range=Optional[str])

slots.env_file = Slot(uri=CORE.env_file, name="env_file", curie=CORE.curie('env_file'),
                   model_uri=CONTAINERS.env_file, domain=None, range=Optional[str])

slots.path = Slot(uri=UCO-OBSERVABLE.path, name="path", curie=UCO-OBSERVABLE.curie('path'),
                   model_uri=CONTAINERS.path, domain=None, range=Optional[str])

slots.names = Slot(uri=CORE.names, name="names", curie=CORE.curie('names'),
                   model_uri=CONTAINERS.names, domain=None, range=Optional[str])

slots.separator = Slot(uri=CORE.separator, name="separator", curie=CORE.curie('separator'),
                   model_uri=CONTAINERS.separator, domain=None, range=Optional[str])

slots.share = Slot(uri=CORE.share, name="share", curie=CORE.curie('share'),
                   model_uri=CONTAINERS.share, domain=None, range=Optional[str])

slots.new = Slot(uri=CORE.new, name="new", curie=CORE.curie('new'),
                   model_uri=CONTAINERS.new, domain=None, range=Optional[str])

slots.after = Slot(uri=CORE.after, name="after", curie=CORE.curie('after'),
                   model_uri=CONTAINERS.after, domain=None, range=Optional[str])

slots.healthcheck = Slot(uri=CORE.healthcheck, name="healthcheck", curie=CORE.curie('healthcheck'),
                   model_uri=CONTAINERS.healthcheck, domain=None, range=Optional[str])

slots.healthcheck_interval = Slot(uri=CORE.healthcheck_interval, name="healthcheck_interval", curie=CORE.curie('healthcheck_interval'),
                   model_uri=CONTAINERS.healthcheck_interval, domain=None, range=Optional[str])

slots.healthcheck_retries = Slot(uri=CORE.healthcheck_retries, name="healthcheck_retries", curie=CORE.curie('healthcheck_retries'),
                   model_uri=CONTAINERS.healthcheck_retries, domain=None, range=Optional[int])

slots.healthcheck_timeout = Slot(uri=CORE.healthcheck_timeout, name="healthcheck_timeout", curie=CORE.curie('healthcheck_timeout'),
                   model_uri=CONTAINERS.healthcheck_timeout, domain=None, range=Optional[str])

slots.hostname = Slot(uri=UCO-OBSERVABLE.hostname, name="hostname", curie=UCO-OBSERVABLE.curie('hostname'),
                   model_uri=CONTAINERS.hostname, domain=None, range=Optional[str])

slots.http_proxy = Slot(uri=CORE.http_proxy, name="http_proxy", curie=CORE.curie('http_proxy'),
                   model_uri=CONTAINERS.http_proxy, domain=None, range=Optional[str])

slots.init = Slot(uri=CORE.init, name="init", curie=CORE.curie('init'),
                   model_uri=CONTAINERS.init, domain=None, range=Optional[str])

slots.interactive = Slot(uri=CORE.interactive, name="interactive", curie=CORE.curie('interactive'),
                   model_uri=CONTAINERS.interactive, domain=None, range=Optional[Union[bool, Bool]])

slots.ip = Slot(uri=UCO-OBSERVABLE.ip, name="ip", curie=UCO-OBSERVABLE.curie('ip'),
                   model_uri=CONTAINERS.ip, domain=None, range=Optional[str])

slots.label = Slot(uri=CORE.label, name="label", curie=CORE.curie('label'),
                   model_uri=CONTAINERS.label, domain=None, range=Optional[str])

slots.log_driver = Slot(uri=CORE.log_driver, name="log_driver", curie=CORE.curie('log_driver'),
                   model_uri=CONTAINERS.log_driver, domain=None, range=Optional[str])

slots.log_level = Slot(uri=CORE.log_level, name="log_level", curie=CORE.curie('log_level'),
                   model_uri=CONTAINERS.log_level, domain=None, range=Optional[str])

slots.max_size = Slot(uri=CORE.max_size, name="max_size", curie=CORE.curie('max_size'),
                   model_uri=CONTAINERS.max_size, domain=None, range=Optional[str])

slots.mac_address = Slot(uri=CORE.mac_address, name="mac_address", curie=CORE.curie('mac_address'),
                   model_uri=CONTAINERS.mac_address, domain=None, range=Optional[str])

slots.memory = Slot(uri=CORE.memory, name="memory", curie=CORE.curie('memory'),
                   model_uri=CONTAINERS.memory, domain=None, range=Optional[str])

slots.mount = Slot(uri=CORE.mount, name="mount", curie=CORE.curie('mount'),
                   model_uri=CONTAINERS.mount, domain=None, range=Optional[Union[str, List[str]]])

slots.network = Slot(uri=UCO-OBSERVABLE.network, name="network", curie=UCO-OBSERVABLE.curie('network'),
                   model_uri=CONTAINERS.network, domain=None, range=Optional[str])

slots.pid = Slot(uri=UCO-OBSERVABLE.pid, name="pid", curie=UCO-OBSERVABLE.curie('pid'),
                   model_uri=CONTAINERS.pid, domain=None, range=Optional[str])

slots.privileged = Slot(uri=CORE.privileged, name="privileged", curie=CORE.curie('privileged'),
                   model_uri=CONTAINERS.privileged, domain=None, range=Optional[Union[bool, Bool]])

slots.publish = Slot(uri=CORE.publish, name="publish", curie=CORE.curie('publish'),
                   model_uri=CONTAINERS.publish, domain=None, range=Optional[Union[str, List[str]]])

slots.read_only = Slot(uri=CORE.read_only, name="read_only", curie=CORE.curie('read_only'),
                   model_uri=CONTAINERS.read_only, domain=None, range=Optional[Union[bool, Bool]])

slots.recreate = Slot(uri=CORE.recreate, name="recreate", curie=CORE.curie('recreate'),
                   model_uri=CONTAINERS.recreate, domain=None, range=Optional[Union[bool, Bool]])

slots.rm = Slot(uri=CORE.rm, name="rm", curie=CORE.curie('rm'),
                   model_uri=CONTAINERS.rm, domain=None, range=Optional[Union[bool, Bool]])

slots.rootfs = Slot(uri=CORE.rootfs, name="rootfs", curie=CORE.curie('rootfs'),
                   model_uri=CONTAINERS.rootfs, domain=None, range=Optional[str])

slots.secrets = Slot(uri=CORE.secrets, name="secrets", curie=CORE.curie('secrets'),
                   model_uri=CONTAINERS.secrets, domain=None, range=Optional[Union[str, List[str]]])

slots.sysctl = Slot(uri=CORE.sysctl, name="sysctl", curie=CORE.curie('sysctl'),
                   model_uri=CONTAINERS.sysctl, domain=None, range=Optional[str])

slots.systemd = Slot(uri=CORE.systemd, name="systemd", curie=CORE.curie('systemd'),
                   model_uri=CONTAINERS.systemd, domain=None, range=Optional[str])

slots.timezone = Slot(uri=CORE.timezone, name="timezone", curie=CORE.curie('timezone'),
                   model_uri=CONTAINERS.timezone, domain=None, range=Optional[str])

slots.tmpfs = Slot(uri=CORE.tmpfs, name="tmpfs", curie=CORE.curie('tmpfs'),
                   model_uri=CONTAINERS.tmpfs, domain=None, range=Optional[str])

slots.tty = Slot(uri=CORE.tty, name="tty", curie=CORE.curie('tty'),
                   model_uri=CONTAINERS.tty, domain=None, range=Optional[str])

slots.ulimit = Slot(uri=CORE.ulimit, name="ulimit", curie=CORE.curie('ulimit'),
                   model_uri=CONTAINERS.ulimit, domain=None, range=Optional[str])

slots.user = Slot(uri=CORE.user, name="user", curie=CORE.curie('user'),
                   model_uri=CONTAINERS.user, domain=None, range=Optional[str])

slots.uts = Slot(uri=CORE.uts, name="uts", curie=CORE.curie('uts'),
                   model_uri=CONTAINERS.uts, domain=None, range=Optional[str])

slots.volume = Slot(uri=UCO-OBSERVABLE.volume, name="volume", curie=UCO-OBSERVABLE.curie('volume'),
                   model_uri=CONTAINERS.volume, domain=Publication, range=Optional[str])

slots.workdir = Slot(uri=CORE.workdir, name="workdir", curie=CORE.curie('workdir'),
                   model_uri=CONTAINERS.workdir, domain=None, range=Optional[str])

slots.cert_dir = Slot(uri=CORE.cert_dir, name="cert_dir", curie=CORE.curie('cert_dir'),
                   model_uri=CONTAINERS.cert_dir, domain=None, range=Optional[str])

slots.force = Slot(uri=CORE.force, name="force", curie=CORE.curie('force'),
                   model_uri=CONTAINERS.force, domain=None, range=Optional[str])

slots.cache = Slot(uri=CORE.cache, name="cache", curie=CORE.curie('cache'),
                   model_uri=CONTAINERS.cache, domain=None, range=Optional[str])

slots.file = Slot(uri=CORE.file, name="file", curie=CORE.curie('file'),
                   model_uri=CONTAINERS.file, domain=Software, range=Optional[str])

slots.format = Slot(uri=UCO-OBSERVABLE.format, name="format", curie=UCO-OBSERVABLE.curie('format'),
                   model_uri=CONTAINERS.format, domain=InformationContentEntity, range=Optional[str])

slots.password = Slot(uri=UCO-OBSERVABLE.password, name="password", curie=UCO-OBSERVABLE.curie('password'),
                   model_uri=CONTAINERS.password, domain=None, range=Optional[str])

slots.compress = Slot(uri=CORE.compress, name="compress", curie=CORE.curie('compress'),
                   model_uri=CONTAINERS.compress, domain=None, range=Optional[str])

slots.dest = Slot(uri=CORE.dest, name="dest", curie=CORE.curie('dest'),
                   model_uri=CONTAINERS.dest, domain=None, range=Optional[str])

slots.transport = Slot(uri=CORE.transport, name="transport", curie=CORE.curie('transport'),
                   model_uri=CONTAINERS.transport, domain=None, range=Optional[str])

slots.username = Slot(uri=CORE.username, name="username", curie=CORE.curie('username'),
                   model_uri=CONTAINERS.username, domain=None, range=Optional[str])

slots.validate_certs = Slot(uri=CORE.validate_certs, name="validate_certs", curie=CORE.curie('validate_certs'),
                   model_uri=CONTAINERS.validate_certs, domain=None, range=Optional[str])

slots.change = Slot(uri=CORE.change, name="change", curie=CORE.curie('change'),
                   model_uri=CONTAINERS.change, domain=None, range=Optional[str])

slots.commit_message = Slot(uri=CORE.commit_message, name="commit_message", curie=CORE.curie('commit_message'),
                   model_uri=CONTAINERS.commit_message, domain=None, range=Optional[str])

slots.src = Slot(uri=UCO-OBSERVABLE.src, name="src", curie=UCO-OBSERVABLE.curie('src'),
                   model_uri=CONTAINERS.src, domain=None, range=Optional[str])

slots.input = Slot(uri=CORE.input, name="input", curie=CORE.curie('input'),
                   model_uri=CONTAINERS.input, domain=None, range=Optional[str])

slots.certdir = Slot(uri=CORE.certdir, name="certdir", curie=CORE.curie('certdir'),
                   model_uri=CONTAINERS.certdir, domain=None, range=Optional[str])

slots.tlsverify = Slot(uri=CORE.tlsverify, name="tlsverify", curie=CORE.curie('tlsverify'),
                   model_uri=CONTAINERS.tlsverify, domain=None, range=Optional[str])

slots.tls_verify = Slot(uri=CORE.tls_verify, name="tls_verify", curie=CORE.curie('tls_verify'),
                   model_uri=CONTAINERS.tls_verify, domain=None, range=Optional[str])

slots.driver = Slot(uri=CORE.driver, name="driver", curie=CORE.curie('driver'),
                   model_uri=CONTAINERS.driver, domain=None, range=Optional[str])

slots.gateway = Slot(uri=CORE.gateway, name="gateway", curie=CORE.curie('gateway'),
                   model_uri=CONTAINERS.gateway, domain=None, range=Optional[str])

slots.internal = Slot(uri=CORE.internal, name="internal", curie=CORE.curie('internal'),
                   model_uri=CONTAINERS.internal, domain=None, range=Optional[str])

slots.ip_range = Slot(uri=CORE.ip_range, name="ip_range", curie=CORE.curie('ip_range'),
                   model_uri=CONTAINERS.ip_range, domain=None, range=Optional[str])

slots.ipv6 = Slot(uri=CORE.ipv6, name="ipv6", curie=CORE.curie('ipv6'),
                   model_uri=CONTAINERS.ipv6, domain=None, range=Optional[str])

slots.opt = Slot(uri=CORE.opt, name="opt", curie=CORE.curie('opt'),
                   model_uri=CONTAINERS.opt, domain=None, range=Optional[str])

slots.mtu = Slot(uri=CORE.mtu, name="mtu", curie=CORE.curie('mtu'),
                   model_uri=CONTAINERS.mtu, domain=None, range=Optional[str])

slots.vlan = Slot(uri=CORE.vlan, name="vlan", curie=CORE.curie('vlan'),
                   model_uri=CONTAINERS.vlan, domain=None, range=Optional[str])

slots.subnet = Slot(uri=CORE.subnet, name="subnet", curie=CORE.curie('subnet'),
                   model_uri=CONTAINERS.subnet, domain=None, range=Optional[str])

slots.quiet = Slot(uri=CORE.quiet, name="quiet", curie=CORE.curie('quiet'),
                   model_uri=CONTAINERS.quiet, domain=None, range=Optional[str])

slots.infra = Slot(uri=CORE.infra, name="infra", curie=CORE.curie('infra'),
                   model_uri=CONTAINERS.infra, domain=None, range=Optional[str])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=CONTAINERS.subject, domain=Association, range=Union[str, NamedThingId])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=CONTAINERS.object, domain=Association, range=Union[str, NamedThingId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=CONTAINERS.predicate, domain=Association, range=Union[str, PredicateType])

slots.negated = Slot(uri=CORE.negated, name="negated", curie=CORE.curie('negated'),
                   model_uri=CONTAINERS.negated, domain=Association, range=Optional[Union[bool, Bool]])

slots.qualifiers = Slot(uri=CORE.qualifiers, name="qualifiers", curie=CORE.curie('qualifiers'),
                   model_uri=CONTAINERS.qualifiers, domain=Association, range=Optional[Union[Union[dict, OntologyClass], List[Union[dict, OntologyClass]]]])

slots.publications = Slot(uri=CORE.publications, name="publications", curie=CORE.curie('publications'),
                   model_uri=CONTAINERS.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.hasEvidence = Slot(uri=CORE.hasEvidence, name="hasEvidence", curie=CORE.curie('hasEvidence'),
                   model_uri=CONTAINERS.hasEvidence, domain=Association, range=Optional[Union[Union[str, EvidenceTypeId], List[Union[str, EvidenceTypeId]]]])

slots.license = Slot(uri=CORE.license, name="license", curie=CORE.curie('license'),
                   model_uri=CONTAINERS.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=CORE.rights, name="rights", curie=CORE.curie('rights'),
                   model_uri=CONTAINERS.rights, domain=InformationContentEntity, range=Optional[str])

slots.authors = Slot(uri=CORE.authors, name="authors", curie=CORE.curie('authors'),
                   model_uri=CONTAINERS.authors, domain=Publication, range=Optional[Union[str, List[str]]])

slots.pages = Slot(uri=CORE.pages, name="pages", curie=CORE.curie('pages'),
                   model_uri=CONTAINERS.pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.summary = Slot(uri=CORE.summary, name="summary", curie=CORE.curie('summary'),
                   model_uri=CONTAINERS.summary, domain=Publication, range=Optional[str])

slots.keywords = Slot(uri=CORE.keywords, name="keywords", curie=CORE.curie('keywords'),
                   model_uri=CONTAINERS.keywords, domain=Publication, range=Optional[Union[str, List[str]]])

slots.lcshTerms = Slot(uri=CORE.lcshTerms, name="lcshTerms", curie=CORE.curie('lcshTerms'),
                   model_uri=CONTAINERS.lcshTerms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.driver_opts = Slot(uri=CORE.driver_opts, name="driver_opts", curie=CORE.curie('driver_opts'),
                   model_uri=CONTAINERS.driver_opts, domain=None, range=Optional[str])

slots.options = Slot(uri=CORE.options, name="options", curie=CORE.curie('options'),
                   model_uri=CONTAINERS.options, domain=None, range=Optional[str])

slots.PodmanContainer_annotation = Slot(uri=CORE.annotation, name="PodmanContainer_annotation", curie=CORE.curie('annotation'),
                   model_uri=CONTAINERS.PodmanContainer_annotation, domain=PodmanContainer, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanContainer_authfile = Slot(uri=CORE.authfile, name="PodmanContainer_authfile", curie=CORE.curie('authfile'),
                   model_uri=CONTAINERS.PodmanContainer_authfile, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_blkio_weight = Slot(uri=CONTAINERS.blkio_weight, name="PodmanContainer_blkio_weight", curie=CONTAINERS.curie('blkio_weight'),
                   model_uri=CONTAINERS.PodmanContainer_blkio_weight, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_blkio_weight_device = Slot(uri=CONTAINERS.blkio_weight_device, name="PodmanContainer_blkio_weight_device", curie=CONTAINERS.curie('blkio_weight_device'),
                   model_uri=CONTAINERS.PodmanContainer_blkio_weight_device, domain=PodmanContainer, range=Optional[Union[Union[dict, "MetaObject"], List[Union[dict, "MetaObject"]]]])

slots.PodmanContainer_cap_add = Slot(uri=CONTAINERS.cap_add, name="PodmanContainer_cap_add", curie=CONTAINERS.curie('cap_add'),
                   model_uri=CONTAINERS.PodmanContainer_cap_add, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_cap_drop = Slot(uri=CONTAINERS.cap_drop, name="PodmanContainer_cap_drop", curie=CONTAINERS.curie('cap_drop'),
                   model_uri=CONTAINERS.PodmanContainer_cap_drop, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_cgroup_parent = Slot(uri=CONTAINERS.cgroup_parent, name="PodmanContainer_cgroup_parent", curie=CONTAINERS.curie('cgroup_parent'),
                   model_uri=CONTAINERS.PodmanContainer_cgroup_parent, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_cgroupns = Slot(uri=CONTAINERS.cgroupns, name="PodmanContainer_cgroupns", curie=CONTAINERS.curie('cgroupns'),
                   model_uri=CONTAINERS.PodmanContainer_cgroupns, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_cgroups = Slot(uri=CORE.cgroups, name="PodmanContainer_cgroups", curie=CORE.curie('cgroups'),
                   model_uri=CONTAINERS.PodmanContainer_cgroups, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_cidfile = Slot(uri=CONTAINERS.cidfile, name="PodmanContainer_cidfile", curie=CONTAINERS.curie('cidfile'),
                   model_uri=CONTAINERS.PodmanContainer_cidfile, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_cmd_args = Slot(uri=CORE.cmd_args, name="PodmanContainer_cmd_args", curie=CORE.curie('cmd_args'),
                   model_uri=CONTAINERS.PodmanContainer_cmd_args, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_command = Slot(uri=CORE.command, name="PodmanContainer_command", curie=CORE.curie('command'),
                   model_uri=CONTAINERS.PodmanContainer_command, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_conmon_pidfile = Slot(uri=CONTAINERS.conmon_pidfile, name="PodmanContainer_conmon_pidfile", curie=CONTAINERS.curie('conmon_pidfile'),
                   model_uri=CONTAINERS.PodmanContainer_conmon_pidfile, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_cpu_period = Slot(uri=CONTAINERS.cpu_period, name="PodmanContainer_cpu_period", curie=CONTAINERS.curie('cpu_period'),
                   model_uri=CONTAINERS.PodmanContainer_cpu_period, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_cpu_rt_period = Slot(uri=CONTAINERS.cpu_rt_period, name="PodmanContainer_cpu_rt_period", curie=CONTAINERS.curie('cpu_rt_period'),
                   model_uri=CONTAINERS.PodmanContainer_cpu_rt_period, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_cpu_rt_runtime = Slot(uri=CONTAINERS.cpu_rt_runtime, name="PodmanContainer_cpu_rt_runtime", curie=CONTAINERS.curie('cpu_rt_runtime'),
                   model_uri=CONTAINERS.PodmanContainer_cpu_rt_runtime, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_cpu_shares = Slot(uri=CONTAINERS.cpu_shares, name="PodmanContainer_cpu_shares", curie=CONTAINERS.curie('cpu_shares'),
                   model_uri=CONTAINERS.PodmanContainer_cpu_shares, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_cpus = Slot(uri=CORE.cpus, name="PodmanContainer_cpus", curie=CORE.curie('cpus'),
                   model_uri=CONTAINERS.PodmanContainer_cpus, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_cpuset_cpus = Slot(uri=CONTAINERS.cpuset_cpus, name="PodmanContainer_cpuset_cpus", curie=CONTAINERS.curie('cpuset_cpus'),
                   model_uri=CONTAINERS.PodmanContainer_cpuset_cpus, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_cpuset_mems = Slot(uri=CONTAINERS.cpuset_mems, name="PodmanContainer_cpuset_mems", curie=CONTAINERS.curie('cpuset_mems'),
                   model_uri=CONTAINERS.PodmanContainer_cpuset_mems, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_debug = Slot(uri=CORE.debug, name="PodmanContainer_debug", curie=CORE.curie('debug'),
                   model_uri=CONTAINERS.PodmanContainer_debug, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_detach = Slot(uri=CONTAINERS.detach, name="PodmanContainer_detach", curie=CONTAINERS.curie('detach'),
                   model_uri=CONTAINERS.PodmanContainer_detach, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_detach_keys = Slot(uri=CONTAINERS.detach_keys, name="PodmanContainer_detach_keys", curie=CONTAINERS.curie('detach_keys'),
                   model_uri=CONTAINERS.PodmanContainer_detach_keys, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_device = Slot(uri=CORE.device, name="PodmanContainer_device", curie=CORE.curie('device'),
                   model_uri=CONTAINERS.PodmanContainer_device, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_device_read_bps = Slot(uri=CONTAINERS.device_read_bps, name="PodmanContainer_device_read_bps", curie=CONTAINERS.curie('device_read_bps'),
                   model_uri=CONTAINERS.PodmanContainer_device_read_bps, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_device_read_iops = Slot(uri=CONTAINERS.device_read_iops, name="PodmanContainer_device_read_iops", curie=CONTAINERS.curie('device_read_iops'),
                   model_uri=CONTAINERS.PodmanContainer_device_read_iops, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_device_write_bps = Slot(uri=CONTAINERS.device_write_bps, name="PodmanContainer_device_write_bps", curie=CONTAINERS.curie('device_write_bps'),
                   model_uri=CONTAINERS.PodmanContainer_device_write_bps, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_device_write_iops = Slot(uri=CONTAINERS.device_write_iops, name="PodmanContainer_device_write_iops", curie=CONTAINERS.curie('device_write_iops'),
                   model_uri=CONTAINERS.PodmanContainer_device_write_iops, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_dns = Slot(uri=CORE.dns, name="PodmanContainer_dns", curie=CORE.curie('dns'),
                   model_uri=CONTAINERS.PodmanContainer_dns, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_dns_option = Slot(uri=CORE.dns_option, name="PodmanContainer_dns_option", curie=CORE.curie('dns_option'),
                   model_uri=CONTAINERS.PodmanContainer_dns_option, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_dns_search = Slot(uri=CORE.dns_search, name="PodmanContainer_dns_search", curie=CORE.curie('dns_search'),
                   model_uri=CONTAINERS.PodmanContainer_dns_search, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_entrypoint = Slot(uri=CONTAINERS.entrypoint, name="PodmanContainer_entrypoint", curie=CONTAINERS.curie('entrypoint'),
                   model_uri=CONTAINERS.PodmanContainer_entrypoint, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_env = Slot(uri=CORE.env, name="PodmanContainer_env", curie=CORE.curie('env'),
                   model_uri=CONTAINERS.PodmanContainer_env, domain=PodmanContainer, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanContainer_env_file = Slot(uri=CORE.env_file, name="PodmanContainer_env_file", curie=CORE.curie('env_file'),
                   model_uri=CONTAINERS.PodmanContainer_env_file, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_env_host = Slot(uri=CONTAINERS.env_host, name="PodmanContainer_env_host", curie=CONTAINERS.curie('env_host'),
                   model_uri=CONTAINERS.PodmanContainer_env_host, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_etc_hosts = Slot(uri=CORE.etc_hosts, name="PodmanContainer_etc_hosts", curie=CORE.curie('etc_hosts'),
                   model_uri=CONTAINERS.PodmanContainer_etc_hosts, domain=PodmanContainer, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanContainer_executable = Slot(uri=CORE.executable, name="PodmanContainer_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanContainer_executable, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_expose = Slot(uri=CONTAINERS.expose, name="PodmanContainer_expose", curie=CONTAINERS.curie('expose'),
                   model_uri=CONTAINERS.PodmanContainer_expose, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_force_restart = Slot(uri=CONTAINERS.force_restart, name="PodmanContainer_force_restart", curie=CONTAINERS.curie('force_restart'),
                   model_uri=CONTAINERS.PodmanContainer_force_restart, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_generate_systemd = Slot(uri=CONTAINERS.generate_systemd, name="PodmanContainer_generate_systemd", curie=CONTAINERS.curie('generate_systemd'),
                   model_uri=CONTAINERS.PodmanContainer_generate_systemd, domain=PodmanContainer, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanContainer_gidmap = Slot(uri=CONTAINERS.gidmap, name="PodmanContainer_gidmap", curie=CONTAINERS.curie('gidmap'),
                   model_uri=CONTAINERS.PodmanContainer_gidmap, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_group_add = Slot(uri=CONTAINERS.group_add, name="PodmanContainer_group_add", curie=CONTAINERS.curie('group_add'),
                   model_uri=CONTAINERS.PodmanContainer_group_add, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_healthcheck = Slot(uri=CORE.healthcheck, name="PodmanContainer_healthcheck", curie=CORE.curie('healthcheck'),
                   model_uri=CONTAINERS.PodmanContainer_healthcheck, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_healthcheck_interval = Slot(uri=CORE.healthcheck_interval, name="PodmanContainer_healthcheck_interval", curie=CORE.curie('healthcheck_interval'),
                   model_uri=CONTAINERS.PodmanContainer_healthcheck_interval, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_healthcheck_retries = Slot(uri=CORE.healthcheck_retries, name="PodmanContainer_healthcheck_retries", curie=CORE.curie('healthcheck_retries'),
                   model_uri=CONTAINERS.PodmanContainer_healthcheck_retries, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_healthcheck_start_period = Slot(uri=CONTAINERS.healthcheck_start_period, name="PodmanContainer_healthcheck_start_period", curie=CONTAINERS.curie('healthcheck_start_period'),
                   model_uri=CONTAINERS.PodmanContainer_healthcheck_start_period, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_healthcheck_timeout = Slot(uri=CORE.healthcheck_timeout, name="PodmanContainer_healthcheck_timeout", curie=CORE.curie('healthcheck_timeout'),
                   model_uri=CONTAINERS.PodmanContainer_healthcheck_timeout, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_hostname = Slot(uri=UCO-OBSERVABLE.hostname, name="PodmanContainer_hostname", curie=UCO-OBSERVABLE.curie('hostname'),
                   model_uri=CONTAINERS.PodmanContainer_hostname, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_http_proxy = Slot(uri=CORE.http_proxy, name="PodmanContainer_http_proxy", curie=CORE.curie('http_proxy'),
                   model_uri=CONTAINERS.PodmanContainer_http_proxy, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_image = Slot(uri=CORE.image, name="PodmanContainer_image", curie=CORE.curie('image'),
                   model_uri=CONTAINERS.PodmanContainer_image, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_image_strict = Slot(uri=CONTAINERS.image_strict, name="PodmanContainer_image_strict", curie=CONTAINERS.curie('image_strict'),
                   model_uri=CONTAINERS.PodmanContainer_image_strict, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_image_volume = Slot(uri=CONTAINERS.image_volume, name="PodmanContainer_image_volume", curie=CONTAINERS.curie('image_volume'),
                   model_uri=CONTAINERS.PodmanContainer_image_volume, domain=PodmanContainer, range=Optional[Union[str, "ContainerImageVolumeEnum"]])

slots.PodmanContainer_init = Slot(uri=CORE.init, name="PodmanContainer_init", curie=CORE.curie('init'),
                   model_uri=CONTAINERS.PodmanContainer_init, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_init_path = Slot(uri=CONTAINERS.init_path, name="PodmanContainer_init_path", curie=CONTAINERS.curie('init_path'),
                   model_uri=CONTAINERS.PodmanContainer_init_path, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_interactive = Slot(uri=CORE.interactive, name="PodmanContainer_interactive", curie=CORE.curie('interactive'),
                   model_uri=CONTAINERS.PodmanContainer_interactive, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_ip = Slot(uri=UCO-OBSERVABLE.ip, name="PodmanContainer_ip", curie=UCO-OBSERVABLE.curie('ip'),
                   model_uri=CONTAINERS.PodmanContainer_ip, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_ipc = Slot(uri=CONTAINERS.ipc, name="PodmanContainer_ipc", curie=CONTAINERS.curie('ipc'),
                   model_uri=CONTAINERS.PodmanContainer_ipc, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_kernel_memory = Slot(uri=CONTAINERS.kernel_memory, name="PodmanContainer_kernel_memory", curie=CONTAINERS.curie('kernel_memory'),
                   model_uri=CONTAINERS.PodmanContainer_kernel_memory, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_label = Slot(uri=CORE.label, name="PodmanContainer_label", curie=CORE.curie('label'),
                   model_uri=CONTAINERS.PodmanContainer_label, domain=PodmanContainer, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanContainer_label_file = Slot(uri=CONTAINERS.label_file, name="PodmanContainer_label_file", curie=CONTAINERS.curie('label_file'),
                   model_uri=CONTAINERS.PodmanContainer_label_file, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_log_driver = Slot(uri=CORE.log_driver, name="PodmanContainer_log_driver", curie=CORE.curie('log_driver'),
                   model_uri=CONTAINERS.PodmanContainer_log_driver, domain=PodmanContainer, range=Optional[Union[str, "ContainerLogDriverEnum"]])

slots.PodmanContainer_log_level = Slot(uri=CORE.log_level, name="PodmanContainer_log_level", curie=CORE.curie('log_level'),
                   model_uri=CONTAINERS.PodmanContainer_log_level, domain=PodmanContainer, range=Optional[Union[str, "ContainerLogLevelEnum"]])

slots.PodmanContainer_log_opt = Slot(uri=CONTAINERS.log_opt, name="PodmanContainer_log_opt", curie=CONTAINERS.curie('log_opt'),
                   model_uri=CONTAINERS.PodmanContainer_log_opt, domain=PodmanContainer, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanContainer_mac_address = Slot(uri=CORE.mac_address, name="PodmanContainer_mac_address", curie=CORE.curie('mac_address'),
                   model_uri=CONTAINERS.PodmanContainer_mac_address, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_memory = Slot(uri=CORE.memory, name="PodmanContainer_memory", curie=CORE.curie('memory'),
                   model_uri=CONTAINERS.PodmanContainer_memory, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_memory_reservation = Slot(uri=CONTAINERS.memory_reservation, name="PodmanContainer_memory_reservation", curie=CONTAINERS.curie('memory_reservation'),
                   model_uri=CONTAINERS.PodmanContainer_memory_reservation, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_memory_swap = Slot(uri=CONTAINERS.memory_swap, name="PodmanContainer_memory_swap", curie=CONTAINERS.curie('memory_swap'),
                   model_uri=CONTAINERS.PodmanContainer_memory_swap, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_memory_swappiness = Slot(uri=CONTAINERS.memory_swappiness, name="PodmanContainer_memory_swappiness", curie=CONTAINERS.curie('memory_swappiness'),
                   model_uri=CONTAINERS.PodmanContainer_memory_swappiness, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_mount = Slot(uri=CORE.mount, name="PodmanContainer_mount", curie=CORE.curie('mount'),
                   model_uri=CONTAINERS.PodmanContainer_mount, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_name = Slot(uri=RDFS.label, name="PodmanContainer_name", curie=RDFS.curie('label'),
                   model_uri=CONTAINERS.PodmanContainer_name, domain=PodmanContainer, range=Union[str, LabelType])

slots.PodmanContainer_network = Slot(uri=UCO-OBSERVABLE.network, name="PodmanContainer_network", curie=UCO-OBSERVABLE.curie('network'),
                   model_uri=CONTAINERS.PodmanContainer_network, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_network_aliases = Slot(uri=CONTAINERS.network_aliases, name="PodmanContainer_network_aliases", curie=CONTAINERS.curie('network_aliases'),
                   model_uri=CONTAINERS.PodmanContainer_network_aliases, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_no_hosts = Slot(uri=CONTAINERS.no_hosts, name="PodmanContainer_no_hosts", curie=CONTAINERS.curie('no_hosts'),
                   model_uri=CONTAINERS.PodmanContainer_no_hosts, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_oom_kill_disable = Slot(uri=CONTAINERS.oom_kill_disable, name="PodmanContainer_oom_kill_disable", curie=CONTAINERS.curie('oom_kill_disable'),
                   model_uri=CONTAINERS.PodmanContainer_oom_kill_disable, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_oom_score_adj = Slot(uri=CONTAINERS.oom_score_adj, name="PodmanContainer_oom_score_adj", curie=CONTAINERS.curie('oom_score_adj'),
                   model_uri=CONTAINERS.PodmanContainer_oom_score_adj, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_pid = Slot(uri=UCO-OBSERVABLE.pid, name="PodmanContainer_pid", curie=UCO-OBSERVABLE.curie('pid'),
                   model_uri=CONTAINERS.PodmanContainer_pid, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_pids_limit = Slot(uri=CONTAINERS.pids_limit, name="PodmanContainer_pids_limit", curie=CONTAINERS.curie('pids_limit'),
                   model_uri=CONTAINERS.PodmanContainer_pids_limit, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_pod = Slot(uri=CONTAINERS.pod, name="PodmanContainer_pod", curie=CONTAINERS.curie('pod'),
                   model_uri=CONTAINERS.PodmanContainer_pod, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_privileged = Slot(uri=CORE.privileged, name="PodmanContainer_privileged", curie=CORE.curie('privileged'),
                   model_uri=CONTAINERS.PodmanContainer_privileged, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_publish = Slot(uri=CORE.publish, name="PodmanContainer_publish", curie=CORE.curie('publish'),
                   model_uri=CONTAINERS.PodmanContainer_publish, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_publish_all = Slot(uri=CONTAINERS.publish_all, name="PodmanContainer_publish_all", curie=CONTAINERS.curie('publish_all'),
                   model_uri=CONTAINERS.PodmanContainer_publish_all, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_read_only = Slot(uri=CORE.read_only, name="PodmanContainer_read_only", curie=CORE.curie('read_only'),
                   model_uri=CONTAINERS.PodmanContainer_read_only, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_read_only_tmpfs = Slot(uri=CONTAINERS.read_only_tmpfs, name="PodmanContainer_read_only_tmpfs", curie=CONTAINERS.curie('read_only_tmpfs'),
                   model_uri=CONTAINERS.PodmanContainer_read_only_tmpfs, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_recreate = Slot(uri=CORE.recreate, name="PodmanContainer_recreate", curie=CORE.curie('recreate'),
                   model_uri=CONTAINERS.PodmanContainer_recreate, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_requires = Slot(uri=CONTAINERS.requires, name="PodmanContainer_requires", curie=CONTAINERS.curie('requires'),
                   model_uri=CONTAINERS.PodmanContainer_requires, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_restart_policy = Slot(uri=CONTAINERS.restart_policy, name="PodmanContainer_restart_policy", curie=CONTAINERS.curie('restart_policy'),
                   model_uri=CONTAINERS.PodmanContainer_restart_policy, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_rm = Slot(uri=CORE.rm, name="PodmanContainer_rm", curie=CORE.curie('rm'),
                   model_uri=CONTAINERS.PodmanContainer_rm, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_rootfs = Slot(uri=CORE.rootfs, name="PodmanContainer_rootfs", curie=CORE.curie('rootfs'),
                   model_uri=CONTAINERS.PodmanContainer_rootfs, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_sdnotify = Slot(uri=CONTAINERS.sdnotify, name="PodmanContainer_sdnotify", curie=CONTAINERS.curie('sdnotify'),
                   model_uri=CONTAINERS.PodmanContainer_sdnotify, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_secrets = Slot(uri=CORE.secrets, name="PodmanContainer_secrets", curie=CORE.curie('secrets'),
                   model_uri=CONTAINERS.PodmanContainer_secrets, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_security_opt = Slot(uri=CONTAINERS.security_opt, name="PodmanContainer_security_opt", curie=CONTAINERS.curie('security_opt'),
                   model_uri=CONTAINERS.PodmanContainer_security_opt, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_shm_size = Slot(uri=CONTAINERS.shm_size, name="PodmanContainer_shm_size", curie=CONTAINERS.curie('shm_size'),
                   model_uri=CONTAINERS.PodmanContainer_shm_size, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_sig_proxy = Slot(uri=CONTAINERS.sig_proxy, name="PodmanContainer_sig_proxy", curie=CONTAINERS.curie('sig_proxy'),
                   model_uri=CONTAINERS.PodmanContainer_sig_proxy, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_state = Slot(uri=UCO-OBSERVABLE.state, name="PodmanContainer_state", curie=UCO-OBSERVABLE.curie('state'),
                   model_uri=CONTAINERS.PodmanContainer_state, domain=PodmanContainer, range=Optional[Union[str, "ContainerStateEnum"]])

slots.PodmanContainer_stop_signal = Slot(uri=CONTAINERS.stop_signal, name="PodmanContainer_stop_signal", curie=CONTAINERS.curie('stop_signal'),
                   model_uri=CONTAINERS.PodmanContainer_stop_signal, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_stop_timeout = Slot(uri=CONTAINERS.stop_timeout, name="PodmanContainer_stop_timeout", curie=CONTAINERS.curie('stop_timeout'),
                   model_uri=CONTAINERS.PodmanContainer_stop_timeout, domain=PodmanContainer, range=Optional[int])

slots.PodmanContainer_subgidname = Slot(uri=CONTAINERS.subgidname, name="PodmanContainer_subgidname", curie=CONTAINERS.curie('subgidname'),
                   model_uri=CONTAINERS.PodmanContainer_subgidname, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_subuidname = Slot(uri=CONTAINERS.subuidname, name="PodmanContainer_subuidname", curie=CONTAINERS.curie('subuidname'),
                   model_uri=CONTAINERS.PodmanContainer_subuidname, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_sysctl = Slot(uri=CORE.sysctl, name="PodmanContainer_sysctl", curie=CORE.curie('sysctl'),
                   model_uri=CONTAINERS.PodmanContainer_sysctl, domain=PodmanContainer, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanContainer_systemd = Slot(uri=CORE.systemd, name="PodmanContainer_systemd", curie=CORE.curie('systemd'),
                   model_uri=CONTAINERS.PodmanContainer_systemd, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_timezone = Slot(uri=CORE.timezone, name="PodmanContainer_timezone", curie=CORE.curie('timezone'),
                   model_uri=CONTAINERS.PodmanContainer_timezone, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_tmpfs = Slot(uri=CORE.tmpfs, name="PodmanContainer_tmpfs", curie=CORE.curie('tmpfs'),
                   model_uri=CONTAINERS.PodmanContainer_tmpfs, domain=PodmanContainer, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanContainer_tty = Slot(uri=CORE.tty, name="PodmanContainer_tty", curie=CORE.curie('tty'),
                   model_uri=CONTAINERS.PodmanContainer_tty, domain=PodmanContainer, range=Optional[Union[bool, Bool]])

slots.PodmanContainer_uidmap = Slot(uri=CONTAINERS.uidmap, name="PodmanContainer_uidmap", curie=CONTAINERS.curie('uidmap'),
                   model_uri=CONTAINERS.PodmanContainer_uidmap, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_ulimit = Slot(uri=CORE.ulimit, name="PodmanContainer_ulimit", curie=CORE.curie('ulimit'),
                   model_uri=CONTAINERS.PodmanContainer_ulimit, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_user = Slot(uri=CORE.user, name="PodmanContainer_user", curie=CORE.curie('user'),
                   model_uri=CONTAINERS.PodmanContainer_user, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_userns = Slot(uri=CONTAINERS.userns, name="PodmanContainer_userns", curie=CONTAINERS.curie('userns'),
                   model_uri=CONTAINERS.PodmanContainer_userns, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_uts = Slot(uri=CORE.uts, name="PodmanContainer_uts", curie=CORE.curie('uts'),
                   model_uri=CONTAINERS.PodmanContainer_uts, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainer_volume = Slot(uri=UCO-OBSERVABLE.volume, name="PodmanContainer_volume", curie=UCO-OBSERVABLE.curie('volume'),
                   model_uri=CONTAINERS.PodmanContainer_volume, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_volumes_from = Slot(uri=CONTAINERS.volumes_from, name="PodmanContainer_volumes_from", curie=CONTAINERS.curie('volumes_from'),
                   model_uri=CONTAINERS.PodmanContainer_volumes_from, domain=PodmanContainer, range=Optional[Union[str, List[str]]])

slots.PodmanContainer_workdir = Slot(uri=CORE.workdir, name="PodmanContainer_workdir", curie=CORE.curie('workdir'),
                   model_uri=CONTAINERS.PodmanContainer_workdir, domain=PodmanContainer, range=Optional[str])

slots.PodmanContainers_containers = Slot(uri=CONTAINERS.containers, name="PodmanContainers_containers", curie=CONTAINERS.curie('containers'),
                   model_uri=CONTAINERS.PodmanContainers_containers, domain=PodmanContainers, range=Union[Union[dict, "MetaObject"], List[Union[dict, "MetaObject"]]])

slots.PodmanContainers_debug = Slot(uri=CORE.debug, name="PodmanContainers_debug", curie=CORE.curie('debug'),
                   model_uri=CONTAINERS.PodmanContainers_debug, domain=PodmanContainers, range=Optional[Union[bool, Bool]])

slots.PodmanExport_container = Slot(uri=CORE.container, name="PodmanExport_container", curie=CORE.curie('container'),
                   model_uri=CONTAINERS.PodmanExport_container, domain=PodmanExport, range=str)

slots.PodmanExport_dest = Slot(uri=CORE.dest, name="PodmanExport_dest", curie=CORE.curie('dest'),
                   model_uri=CONTAINERS.PodmanExport_dest, domain=PodmanExport, range=str)

slots.PodmanExport_executable = Slot(uri=CORE.executable, name="PodmanExport_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanExport_executable, domain=PodmanExport, range=Optional[str])

slots.PodmanExport_force = Slot(uri=CORE.force, name="PodmanExport_force", curie=CORE.curie('force'),
                   model_uri=CONTAINERS.PodmanExport_force, domain=PodmanExport, range=Optional[Union[bool, Bool]])

slots.PodmanGenerateSystemd_after = Slot(uri=CORE.after, name="PodmanGenerateSystemd_after", curie=CORE.curie('after'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_after, domain=PodmanGenerateSystemd, range=Optional[Union[str, List[str]]])

slots.PodmanGenerateSystemd_container_prefix = Slot(uri=CONTAINERS.container_prefix, name="PodmanGenerateSystemd_container_prefix", curie=CONTAINERS.curie('container_prefix'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_container_prefix, domain=PodmanGenerateSystemd, range=Optional[str])

slots.PodmanGenerateSystemd_dest = Slot(uri=CORE.dest, name="PodmanGenerateSystemd_dest", curie=CORE.curie('dest'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_dest, domain=PodmanGenerateSystemd, range=Optional[str])

slots.PodmanGenerateSystemd_env = Slot(uri=CORE.env, name="PodmanGenerateSystemd_env", curie=CORE.curie('env'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_env, domain=PodmanGenerateSystemd, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanGenerateSystemd_executable = Slot(uri=CORE.executable, name="PodmanGenerateSystemd_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_executable, domain=PodmanGenerateSystemd, range=Optional[str])

slots.PodmanGenerateSystemd_name = Slot(uri=RDFS.label, name="PodmanGenerateSystemd_name", curie=RDFS.curie('label'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_name, domain=PodmanGenerateSystemd, range=Union[str, LabelType])

slots.PodmanGenerateSystemd_new = Slot(uri=CORE.new, name="PodmanGenerateSystemd_new", curie=CORE.curie('new'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_new, domain=PodmanGenerateSystemd, range=Optional[Union[bool, Bool]])

slots.PodmanGenerateSystemd_no_header = Slot(uri=CONTAINERS.no_header, name="PodmanGenerateSystemd_no_header", curie=CONTAINERS.curie('no_header'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_no_header, domain=PodmanGenerateSystemd, range=Optional[Union[bool, Bool]])

slots.PodmanGenerateSystemd_pod_prefix = Slot(uri=CONTAINERS.pod_prefix, name="PodmanGenerateSystemd_pod_prefix", curie=CONTAINERS.curie('pod_prefix'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_pod_prefix, domain=PodmanGenerateSystemd, range=Optional[str])

slots.PodmanGenerateSystemd_requires = Slot(uri=CONTAINERS.requires, name="PodmanGenerateSystemd_requires", curie=CONTAINERS.curie('requires'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_requires, domain=PodmanGenerateSystemd, range=Optional[Union[str, List[str]]])

slots.PodmanGenerateSystemd_restart_policy = Slot(uri=CONTAINERS.restart_policy, name="PodmanGenerateSystemd_restart_policy", curie=CONTAINERS.curie('restart_policy'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_restart_policy, domain=PodmanGenerateSystemd, range=Optional[Union[str, "ContainerRestartPolicyEnum"]])

slots.PodmanGenerateSystemd_restart_sec = Slot(uri=CONTAINERS.restart_sec, name="PodmanGenerateSystemd_restart_sec", curie=CONTAINERS.curie('restart_sec'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_restart_sec, domain=PodmanGenerateSystemd, range=Optional[int])

slots.PodmanGenerateSystemd_separator = Slot(uri=CORE.separator, name="PodmanGenerateSystemd_separator", curie=CORE.curie('separator'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_separator, domain=PodmanGenerateSystemd, range=Optional[str])

slots.PodmanGenerateSystemd_start_timeout = Slot(uri=CONTAINERS.start_timeout, name="PodmanGenerateSystemd_start_timeout", curie=CONTAINERS.curie('start_timeout'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_start_timeout, domain=PodmanGenerateSystemd, range=Optional[int])

slots.PodmanGenerateSystemd_stop_timeout = Slot(uri=CONTAINERS.stop_timeout, name="PodmanGenerateSystemd_stop_timeout", curie=CONTAINERS.curie('stop_timeout'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_stop_timeout, domain=PodmanGenerateSystemd, range=Optional[int])

slots.PodmanGenerateSystemd_use_names = Slot(uri=CONTAINERS.use_names, name="PodmanGenerateSystemd_use_names", curie=CONTAINERS.curie('use_names'),
                   model_uri=CONTAINERS.PodmanGenerateSystemd_use_names, domain=PodmanGenerateSystemd, range=Optional[Union[bool, Bool]])

slots.PodmanImage_auth_file = Slot(uri=CORE.auth_file, name="PodmanImage_auth_file", curie=CORE.curie('auth_file'),
                   model_uri=CONTAINERS.PodmanImage_auth_file, domain=PodmanImage, range=Optional[str])

slots.PodmanImage_build = Slot(uri=CORE.build, name="PodmanImage_build", curie=CORE.curie('build'),
                   model_uri=CONTAINERS.PodmanImage_build, domain=PodmanImage, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanImage_ca_cert_dir = Slot(uri=CONTAINERS.ca_cert_dir, name="PodmanImage_ca_cert_dir", curie=CONTAINERS.curie('ca_cert_dir'),
                   model_uri=CONTAINERS.PodmanImage_ca_cert_dir, domain=PodmanImage, range=Optional[str])

slots.PodmanImage_executable = Slot(uri=CORE.executable, name="PodmanImage_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanImage_executable, domain=PodmanImage, range=Optional[str])

slots.PodmanImage_force = Slot(uri=CORE.force, name="PodmanImage_force", curie=CORE.curie('force'),
                   model_uri=CONTAINERS.PodmanImage_force, domain=PodmanImage, range=Optional[Union[bool, Bool]])

slots.PodmanImage_name = Slot(uri=RDFS.label, name="PodmanImage_name", curie=RDFS.curie('label'),
                   model_uri=CONTAINERS.PodmanImage_name, domain=PodmanImage, range=Union[str, LabelType])

slots.PodmanImage_password = Slot(uri=UCO-OBSERVABLE.password, name="PodmanImage_password", curie=UCO-OBSERVABLE.curie('password'),
                   model_uri=CONTAINERS.PodmanImage_password, domain=PodmanImage, range=Optional[str])

slots.PodmanImage_path = Slot(uri=UCO-OBSERVABLE.path, name="PodmanImage_path", curie=UCO-OBSERVABLE.curie('path'),
                   model_uri=CONTAINERS.PodmanImage_path, domain=PodmanImage, range=Optional[str])

slots.PodmanImage_pull = Slot(uri=CONTAINERS.pull, name="PodmanImage_pull", curie=CONTAINERS.curie('pull'),
                   model_uri=CONTAINERS.PodmanImage_pull, domain=PodmanImage, range=Optional[Union[bool, Bool]])

slots.PodmanImage_push = Slot(uri=CONTAINERS.push, name="PodmanImage_push", curie=CONTAINERS.curie('push'),
                   model_uri=CONTAINERS.PodmanImage_push, domain=PodmanImage, range=Optional[Union[bool, Bool]])

slots.PodmanImage_push_args = Slot(uri=CONTAINERS.push_args, name="PodmanImage_push_args", curie=CONTAINERS.curie('push_args'),
                   model_uri=CONTAINERS.PodmanImage_push_args, domain=PodmanImage, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanImage_state = Slot(uri=UCO-OBSERVABLE.state, name="PodmanImage_state", curie=UCO-OBSERVABLE.curie('state'),
                   model_uri=CONTAINERS.PodmanImage_state, domain=PodmanImage, range=Optional[Union[str, "ContainerImageStateEnum"]])

slots.PodmanImage_tag = Slot(uri=CORE.tag, name="PodmanImage_tag", curie=CORE.curie('tag'),
                   model_uri=CONTAINERS.PodmanImage_tag, domain=PodmanImage, range=Optional[str])

slots.PodmanImage_username = Slot(uri=CORE.username, name="PodmanImage_username", curie=CORE.curie('username'),
                   model_uri=CONTAINERS.PodmanImage_username, domain=PodmanImage, range=Optional[str])

slots.PodmanImage_validate_certs = Slot(uri=CORE.validate_certs, name="PodmanImage_validate_certs", curie=CORE.curie('validate_certs'),
                   model_uri=CONTAINERS.PodmanImage_validate_certs, domain=PodmanImage, range=Optional[Union[bool, Bool]])

slots.PodmanImport_change = Slot(uri=CORE.change, name="PodmanImport_change", curie=CORE.curie('change'),
                   model_uri=CONTAINERS.PodmanImport_change, domain=PodmanImport, range=Optional[Union[Union[dict, "MetaObject"], List[Union[dict, "MetaObject"]]]])

slots.PodmanImport_commit_message = Slot(uri=CORE.commit_message, name="PodmanImport_commit_message", curie=CORE.curie('commit_message'),
                   model_uri=CONTAINERS.PodmanImport_commit_message, domain=PodmanImport, range=Optional[str])

slots.PodmanImport_executable = Slot(uri=CORE.executable, name="PodmanImport_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanImport_executable, domain=PodmanImport, range=Optional[str])

slots.PodmanImport_src = Slot(uri=UCO-OBSERVABLE.src, name="PodmanImport_src", curie=UCO-OBSERVABLE.curie('src'),
                   model_uri=CONTAINERS.PodmanImport_src, domain=PodmanImport, range=str)

slots.PodmanLoad_executable = Slot(uri=CORE.executable, name="PodmanLoad_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanLoad_executable, domain=PodmanLoad, range=Optional[str])

slots.PodmanLoad_input = Slot(uri=CORE.input, name="PodmanLoad_input", curie=CORE.curie('input'),
                   model_uri=CONTAINERS.PodmanLoad_input, domain=PodmanLoad, range=str)

slots.PodmanLogin_authfile = Slot(uri=CORE.authfile, name="PodmanLogin_authfile", curie=CORE.curie('authfile'),
                   model_uri=CONTAINERS.PodmanLogin_authfile, domain=PodmanLogin, range=Optional[str])

slots.PodmanLogin_certdir = Slot(uri=CORE.certdir, name="PodmanLogin_certdir", curie=CORE.curie('certdir'),
                   model_uri=CONTAINERS.PodmanLogin_certdir, domain=PodmanLogin, range=Optional[str])

slots.PodmanLogin_executable = Slot(uri=CORE.executable, name="PodmanLogin_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanLogin_executable, domain=PodmanLogin, range=Optional[str])

slots.PodmanLogin_password = Slot(uri=UCO-OBSERVABLE.password, name="PodmanLogin_password", curie=UCO-OBSERVABLE.curie('password'),
                   model_uri=CONTAINERS.PodmanLogin_password, domain=PodmanLogin, range=str)

slots.PodmanLogin_registry = Slot(uri=CONTAINERS.registry, name="PodmanLogin_registry", curie=CONTAINERS.curie('registry'),
                   model_uri=CONTAINERS.PodmanLogin_registry, domain=PodmanLogin, range=Optional[str])

slots.PodmanLogin_tlsverify = Slot(uri=CORE.tlsverify, name="PodmanLogin_tlsverify", curie=CORE.curie('tlsverify'),
                   model_uri=CONTAINERS.PodmanLogin_tlsverify, domain=PodmanLogin, range=Optional[Union[bool, Bool]])

slots.PodmanLogin_username = Slot(uri=CORE.username, name="PodmanLogin_username", curie=CORE.curie('username'),
                   model_uri=CONTAINERS.PodmanLogin_username, domain=PodmanLogin, range=str)

slots.PodmanLogout_all = Slot(uri=CONTAINERS.all, name="PodmanLogout_all", curie=CONTAINERS.curie('all'),
                   model_uri=CONTAINERS.PodmanLogout_all, domain=PodmanLogout, range=Optional[Union[bool, Bool]])

slots.PodmanLogout_authfile = Slot(uri=CORE.authfile, name="PodmanLogout_authfile", curie=CORE.curie('authfile'),
                   model_uri=CONTAINERS.PodmanLogout_authfile, domain=PodmanLogout, range=Optional[str])

slots.PodmanLogout_executable = Slot(uri=CORE.executable, name="PodmanLogout_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanLogout_executable, domain=PodmanLogout, range=Optional[str])

slots.PodmanLogout_ignore_docker_credentials = Slot(uri=CONTAINERS.ignore_docker_credentials, name="PodmanLogout_ignore_docker_credentials", curie=CONTAINERS.curie('ignore_docker_credentials'),
                   model_uri=CONTAINERS.PodmanLogout_ignore_docker_credentials, domain=PodmanLogout, range=Optional[Union[bool, Bool]])

slots.PodmanLogout_registry = Slot(uri=CONTAINERS.registry, name="PodmanLogout_registry", curie=CONTAINERS.curie('registry'),
                   model_uri=CONTAINERS.PodmanLogout_registry, domain=PodmanLogout, range=Optional[str])

slots.PodmanNetwork_debug = Slot(uri=CORE.debug, name="PodmanNetwork_debug", curie=CORE.curie('debug'),
                   model_uri=CONTAINERS.PodmanNetwork_debug, domain=PodmanNetwork, range=Optional[Union[bool, Bool]])

slots.PodmanNetwork_disable_dns = Slot(uri=CONTAINERS.disable_dns, name="PodmanNetwork_disable_dns", curie=CONTAINERS.curie('disable_dns'),
                   model_uri=CONTAINERS.PodmanNetwork_disable_dns, domain=PodmanNetwork, range=Optional[Union[bool, Bool]])

slots.PodmanNetwork_driver = Slot(uri=CORE.driver, name="PodmanNetwork_driver", curie=CORE.curie('driver'),
                   model_uri=CONTAINERS.PodmanNetwork_driver, domain=PodmanNetwork, range=Optional[str])

slots.PodmanNetwork_executable = Slot(uri=CORE.executable, name="PodmanNetwork_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanNetwork_executable, domain=PodmanNetwork, range=Optional[str])

slots.PodmanNetwork_gateway = Slot(uri=CORE.gateway, name="PodmanNetwork_gateway", curie=CORE.curie('gateway'),
                   model_uri=CONTAINERS.PodmanNetwork_gateway, domain=PodmanNetwork, range=Optional[str])

slots.PodmanNetwork_internal = Slot(uri=CORE.internal, name="PodmanNetwork_internal", curie=CORE.curie('internal'),
                   model_uri=CONTAINERS.PodmanNetwork_internal, domain=PodmanNetwork, range=Optional[Union[bool, Bool]])

slots.PodmanNetwork_ip_range = Slot(uri=CORE.ip_range, name="PodmanNetwork_ip_range", curie=CORE.curie('ip_range'),
                   model_uri=CONTAINERS.PodmanNetwork_ip_range, domain=PodmanNetwork, range=Optional[str])

slots.PodmanNetwork_ipv6 = Slot(uri=CORE.ipv6, name="PodmanNetwork_ipv6", curie=CORE.curie('ipv6'),
                   model_uri=CONTAINERS.PodmanNetwork_ipv6, domain=PodmanNetwork, range=Optional[Union[bool, Bool]])

slots.PodmanNetwork_macvlan = Slot(uri=CONTAINERS.macvlan, name="PodmanNetwork_macvlan", curie=CONTAINERS.curie('macvlan'),
                   model_uri=CONTAINERS.PodmanNetwork_macvlan, domain=PodmanNetwork, range=Optional[str])

slots.PodmanNetwork_name = Slot(uri=RDFS.label, name="PodmanNetwork_name", curie=RDFS.curie('label'),
                   model_uri=CONTAINERS.PodmanNetwork_name, domain=PodmanNetwork, range=Union[str, LabelType])

slots.PodmanNetwork_opt = Slot(uri=CORE.opt, name="PodmanNetwork_opt", curie=CORE.curie('opt'),
                   model_uri=CONTAINERS.PodmanNetwork_opt, domain=PodmanNetwork, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanNetwork_recreate = Slot(uri=CORE.recreate, name="PodmanNetwork_recreate", curie=CORE.curie('recreate'),
                   model_uri=CONTAINERS.PodmanNetwork_recreate, domain=PodmanNetwork, range=Optional[Union[bool, Bool]])

slots.PodmanNetwork_state = Slot(uri=UCO-OBSERVABLE.state, name="PodmanNetwork_state", curie=UCO-OBSERVABLE.curie('state'),
                   model_uri=CONTAINERS.PodmanNetwork_state, domain=PodmanNetwork, range=Optional[Union[str, "ContainerNetworkStateEnum"]])

slots.PodmanNetwork_subnet = Slot(uri=CORE.subnet, name="PodmanNetwork_subnet", curie=CORE.curie('subnet'),
                   model_uri=CONTAINERS.PodmanNetwork_subnet, domain=PodmanNetwork, range=Optional[str])

slots.PodmanPlay_authfile = Slot(uri=CORE.authfile, name="PodmanPlay_authfile", curie=CORE.curie('authfile'),
                   model_uri=CONTAINERS.PodmanPlay_authfile, domain=PodmanPlay, range=Optional[str])

slots.PodmanPlay_cert_dir = Slot(uri=CORE.cert_dir, name="PodmanPlay_cert_dir", curie=CORE.curie('cert_dir'),
                   model_uri=CONTAINERS.PodmanPlay_cert_dir, domain=PodmanPlay, range=Optional[str])

slots.PodmanPlay_configmap = Slot(uri=CONTAINERS.configmap, name="PodmanPlay_configmap", curie=CONTAINERS.curie('configmap'),
                   model_uri=CONTAINERS.PodmanPlay_configmap, domain=PodmanPlay, range=Optional[Union[str, List[str]]])

slots.PodmanPlay_debug = Slot(uri=CORE.debug, name="PodmanPlay_debug", curie=CORE.curie('debug'),
                   model_uri=CONTAINERS.PodmanPlay_debug, domain=PodmanPlay, range=Optional[Union[bool, Bool]])

slots.PodmanPlay_executable = Slot(uri=CORE.executable, name="PodmanPlay_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanPlay_executable, domain=PodmanPlay, range=Optional[str])

slots.PodmanPlay_kube_file = Slot(uri=CONTAINERS.kube_file, name="PodmanPlay_kube_file", curie=CONTAINERS.curie('kube_file'),
                   model_uri=CONTAINERS.PodmanPlay_kube_file, domain=PodmanPlay, range=str)

slots.PodmanPlay_log_driver = Slot(uri=CORE.log_driver, name="PodmanPlay_log_driver", curie=CORE.curie('log_driver'),
                   model_uri=CONTAINERS.PodmanPlay_log_driver, domain=PodmanPlay, range=Optional[str])

slots.PodmanPlay_log_level = Slot(uri=CORE.log_level, name="PodmanPlay_log_level", curie=CORE.curie('log_level'),
                   model_uri=CONTAINERS.PodmanPlay_log_level, domain=PodmanPlay, range=Optional[Union[str, "ContainerLogLevelEnum"]])

slots.PodmanPlay_network = Slot(uri=UCO-OBSERVABLE.network, name="PodmanPlay_network", curie=UCO-OBSERVABLE.curie('network'),
                   model_uri=CONTAINERS.PodmanPlay_network, domain=PodmanPlay, range=Optional[Union[str, List[str]]])

slots.PodmanPlay_password = Slot(uri=UCO-OBSERVABLE.password, name="PodmanPlay_password", curie=UCO-OBSERVABLE.curie('password'),
                   model_uri=CONTAINERS.PodmanPlay_password, domain=PodmanPlay, range=Optional[str])

slots.PodmanPlay_quiet = Slot(uri=CORE.quiet, name="PodmanPlay_quiet", curie=CORE.curie('quiet'),
                   model_uri=CONTAINERS.PodmanPlay_quiet, domain=PodmanPlay, range=Optional[Union[bool, Bool]])

slots.PodmanPlay_recreate = Slot(uri=CORE.recreate, name="PodmanPlay_recreate", curie=CORE.curie('recreate'),
                   model_uri=CONTAINERS.PodmanPlay_recreate, domain=PodmanPlay, range=Optional[Union[bool, Bool]])

slots.PodmanPlay_seccomp_profile_root = Slot(uri=CONTAINERS.seccomp_profile_root, name="PodmanPlay_seccomp_profile_root", curie=CONTAINERS.curie('seccomp_profile_root'),
                   model_uri=CONTAINERS.PodmanPlay_seccomp_profile_root, domain=PodmanPlay, range=Optional[str])

slots.PodmanPlay_state = Slot(uri=UCO-OBSERVABLE.state, name="PodmanPlay_state", curie=UCO-OBSERVABLE.curie('state'),
                   model_uri=CONTAINERS.PodmanPlay_state, domain=PodmanPlay, range=Union[str, "ContainerStateEnum"])

slots.PodmanPlay_tls_verify = Slot(uri=CORE.tls_verify, name="PodmanPlay_tls_verify", curie=CORE.curie('tls_verify'),
                   model_uri=CONTAINERS.PodmanPlay_tls_verify, domain=PodmanPlay, range=Optional[Union[bool, Bool]])

slots.PodmanPlay_username = Slot(uri=CORE.username, name="PodmanPlay_username", curie=CORE.curie('username'),
                   model_uri=CONTAINERS.PodmanPlay_username, domain=PodmanPlay, range=Optional[str])

slots.PodmanPod_add_host = Slot(uri=CONTAINERS.add_host, name="PodmanPod_add_host", curie=CONTAINERS.curie('add_host'),
                   model_uri=CONTAINERS.PodmanPod_add_host, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_cgroup_parent = Slot(uri=CONTAINERS.cgroup_parent, name="PodmanPod_cgroup_parent", curie=CONTAINERS.curie('cgroup_parent'),
                   model_uri=CONTAINERS.PodmanPod_cgroup_parent, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_cpus = Slot(uri=CORE.cpus, name="PodmanPod_cpus", curie=CORE.curie('cpus'),
                   model_uri=CONTAINERS.PodmanPod_cpus, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_cpuset_cpus = Slot(uri=CONTAINERS.cpuset_cpus, name="PodmanPod_cpuset_cpus", curie=CONTAINERS.curie('cpuset_cpus'),
                   model_uri=CONTAINERS.PodmanPod_cpuset_cpus, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_debug = Slot(uri=CORE.debug, name="PodmanPod_debug", curie=CORE.curie('debug'),
                   model_uri=CONTAINERS.PodmanPod_debug, domain=PodmanPod, range=Optional[Union[bool, Bool]])

slots.PodmanPod_device = Slot(uri=CORE.device, name="PodmanPod_device", curie=CORE.curie('device'),
                   model_uri=CONTAINERS.PodmanPod_device, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_device_read_bps = Slot(uri=CONTAINERS.device_read_bps, name="PodmanPod_device_read_bps", curie=CONTAINERS.curie('device_read_bps'),
                   model_uri=CONTAINERS.PodmanPod_device_read_bps, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_dns = Slot(uri=CORE.dns, name="PodmanPod_dns", curie=CORE.curie('dns'),
                   model_uri=CONTAINERS.PodmanPod_dns, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_dns_opt = Slot(uri=CORE.dns_opt, name="PodmanPod_dns_opt", curie=CORE.curie('dns_opt'),
                   model_uri=CONTAINERS.PodmanPod_dns_opt, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_dns_search = Slot(uri=CORE.dns_search, name="PodmanPod_dns_search", curie=CORE.curie('dns_search'),
                   model_uri=CONTAINERS.PodmanPod_dns_search, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_executable = Slot(uri=CORE.executable, name="PodmanPod_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanPod_executable, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_generate_systemd = Slot(uri=CONTAINERS.generate_systemd, name="PodmanPod_generate_systemd", curie=CONTAINERS.curie('generate_systemd'),
                   model_uri=CONTAINERS.PodmanPod_generate_systemd, domain=PodmanPod, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanPod_gidmap = Slot(uri=CONTAINERS.gidmap, name="PodmanPod_gidmap", curie=CONTAINERS.curie('gidmap'),
                   model_uri=CONTAINERS.PodmanPod_gidmap, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_hostname = Slot(uri=UCO-OBSERVABLE.hostname, name="PodmanPod_hostname", curie=UCO-OBSERVABLE.curie('hostname'),
                   model_uri=CONTAINERS.PodmanPod_hostname, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_infra = Slot(uri=CORE.infra, name="PodmanPod_infra", curie=CORE.curie('infra'),
                   model_uri=CONTAINERS.PodmanPod_infra, domain=PodmanPod, range=Optional[Union[bool, Bool]])

slots.PodmanPod_infra_command = Slot(uri=CONTAINERS.infra_command, name="PodmanPod_infra_command", curie=CONTAINERS.curie('infra_command'),
                   model_uri=CONTAINERS.PodmanPod_infra_command, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_infra_conmon_pidfile = Slot(uri=CONTAINERS.infra_conmon_pidfile, name="PodmanPod_infra_conmon_pidfile", curie=CONTAINERS.curie('infra_conmon_pidfile'),
                   model_uri=CONTAINERS.PodmanPod_infra_conmon_pidfile, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_infra_image = Slot(uri=CONTAINERS.infra_image, name="PodmanPod_infra_image", curie=CONTAINERS.curie('infra_image'),
                   model_uri=CONTAINERS.PodmanPod_infra_image, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_infra_name = Slot(uri=CONTAINERS.infra_name, name="PodmanPod_infra_name", curie=CONTAINERS.curie('infra_name'),
                   model_uri=CONTAINERS.PodmanPod_infra_name, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_ip = Slot(uri=UCO-OBSERVABLE.ip, name="PodmanPod_ip", curie=UCO-OBSERVABLE.curie('ip'),
                   model_uri=CONTAINERS.PodmanPod_ip, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_label = Slot(uri=CORE.label, name="PodmanPod_label", curie=CORE.curie('label'),
                   model_uri=CONTAINERS.PodmanPod_label, domain=PodmanPod, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanPod_label_file = Slot(uri=CONTAINERS.label_file, name="PodmanPod_label_file", curie=CONTAINERS.curie('label_file'),
                   model_uri=CONTAINERS.PodmanPod_label_file, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_mac_address = Slot(uri=CORE.mac_address, name="PodmanPod_mac_address", curie=CORE.curie('mac_address'),
                   model_uri=CONTAINERS.PodmanPod_mac_address, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_name = Slot(uri=RDFS.label, name="PodmanPod_name", curie=RDFS.curie('label'),
                   model_uri=CONTAINERS.PodmanPod_name, domain=PodmanPod, range=Union[str, LabelType])

slots.PodmanPod_network = Slot(uri=UCO-OBSERVABLE.network, name="PodmanPod_network", curie=UCO-OBSERVABLE.curie('network'),
                   model_uri=CONTAINERS.PodmanPod_network, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_network_alias = Slot(uri=CONTAINERS.network_alias, name="PodmanPod_network_alias", curie=CONTAINERS.curie('network_alias'),
                   model_uri=CONTAINERS.PodmanPod_network_alias, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_no_hosts = Slot(uri=CONTAINERS.no_hosts, name="PodmanPod_no_hosts", curie=CONTAINERS.curie('no_hosts'),
                   model_uri=CONTAINERS.PodmanPod_no_hosts, domain=PodmanPod, range=Optional[Union[bool, Bool]])

slots.PodmanPod_pid = Slot(uri=UCO-OBSERVABLE.pid, name="PodmanPod_pid", curie=UCO-OBSERVABLE.curie('pid'),
                   model_uri=CONTAINERS.PodmanPod_pid, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_pod_id_file = Slot(uri=CONTAINERS.pod_id_file, name="PodmanPod_pod_id_file", curie=CONTAINERS.curie('pod_id_file'),
                   model_uri=CONTAINERS.PodmanPod_pod_id_file, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_publish = Slot(uri=CORE.publish, name="PodmanPod_publish", curie=CORE.curie('publish'),
                   model_uri=CONTAINERS.PodmanPod_publish, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_recreate = Slot(uri=CORE.recreate, name="PodmanPod_recreate", curie=CORE.curie('recreate'),
                   model_uri=CONTAINERS.PodmanPod_recreate, domain=PodmanPod, range=Optional[Union[bool, Bool]])

slots.PodmanPod_share = Slot(uri=CORE.share, name="PodmanPod_share", curie=CORE.curie('share'),
                   model_uri=CONTAINERS.PodmanPod_share, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_state = Slot(uri=UCO-OBSERVABLE.state, name="PodmanPod_state", curie=UCO-OBSERVABLE.curie('state'),
                   model_uri=CONTAINERS.PodmanPod_state, domain=PodmanPod, range=Optional[Union[str, "ContainerStateEnum"]])

slots.PodmanPod_subgidname = Slot(uri=CONTAINERS.subgidname, name="PodmanPod_subgidname", curie=CONTAINERS.curie('subgidname'),
                   model_uri=CONTAINERS.PodmanPod_subgidname, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_subuidname = Slot(uri=CONTAINERS.subuidname, name="PodmanPod_subuidname", curie=CONTAINERS.curie('subuidname'),
                   model_uri=CONTAINERS.PodmanPod_subuidname, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_uidmap = Slot(uri=CONTAINERS.uidmap, name="PodmanPod_uidmap", curie=CONTAINERS.curie('uidmap'),
                   model_uri=CONTAINERS.PodmanPod_uidmap, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanPod_userns = Slot(uri=CONTAINERS.userns, name="PodmanPod_userns", curie=CONTAINERS.curie('userns'),
                   model_uri=CONTAINERS.PodmanPod_userns, domain=PodmanPod, range=Optional[str])

slots.PodmanPod_volume = Slot(uri=UCO-OBSERVABLE.volume, name="PodmanPod_volume", curie=UCO-OBSERVABLE.curie('volume'),
                   model_uri=CONTAINERS.PodmanPod_volume, domain=PodmanPod, range=Optional[Union[str, List[str]]])

slots.PodmanSave_compress = Slot(uri=CORE.compress, name="PodmanSave_compress", curie=CORE.curie('compress'),
                   model_uri=CONTAINERS.PodmanSave_compress, domain=PodmanSave, range=Optional[Union[bool, Bool]])

slots.PodmanSave_dest = Slot(uri=CORE.dest, name="PodmanSave_dest", curie=CORE.curie('dest'),
                   model_uri=CONTAINERS.PodmanSave_dest, domain=PodmanSave, range=str)

slots.PodmanSave_executable = Slot(uri=CORE.executable, name="PodmanSave_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanSave_executable, domain=PodmanSave, range=Optional[str])

slots.PodmanSave_force = Slot(uri=CORE.force, name="PodmanSave_force", curie=CORE.curie('force'),
                   model_uri=CONTAINERS.PodmanSave_force, domain=PodmanSave, range=Optional[Union[bool, Bool]])

slots.PodmanSave_format = Slot(uri=UCO-OBSERVABLE.format, name="PodmanSave_format", curie=UCO-OBSERVABLE.curie('format'),
                   model_uri=CONTAINERS.PodmanSave_format, domain=PodmanSave, range=Optional[Union[str, "ContainerSaveFormatEnum"]])

slots.PodmanSave_image = Slot(uri=CORE.image, name="PodmanSave_image", curie=CORE.curie('image'),
                   model_uri=CONTAINERS.PodmanSave_image, domain=PodmanSave, range=str)

slots.PodmanSave_multi_image_archive = Slot(uri=CONTAINERS.multi_image_archive, name="PodmanSave_multi_image_archive", curie=CONTAINERS.curie('multi_image_archive'),
                   model_uri=CONTAINERS.PodmanSave_multi_image_archive, domain=PodmanSave, range=Optional[Union[bool, Bool]])

slots.PodmanSecret_data = Slot(uri=UCO-OBSERVABLE.data, name="PodmanSecret_data", curie=UCO-OBSERVABLE.curie('data'),
                   model_uri=CONTAINERS.PodmanSecret_data, domain=PodmanSecret, range=Optional[str])

slots.PodmanSecret_driver = Slot(uri=CORE.driver, name="PodmanSecret_driver", curie=CORE.curie('driver'),
                   model_uri=CONTAINERS.PodmanSecret_driver, domain=PodmanSecret, range=Optional[str])

slots.PodmanSecret_driver_opts = Slot(uri=CORE.driver_opts, name="PodmanSecret_driver_opts", curie=CORE.curie('driver_opts'),
                   model_uri=CONTAINERS.PodmanSecret_driver_opts, domain=PodmanSecret, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanSecret_executable = Slot(uri=CORE.executable, name="PodmanSecret_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanSecret_executable, domain=PodmanSecret, range=Optional[str])

slots.PodmanSecret_force = Slot(uri=CORE.force, name="PodmanSecret_force", curie=CORE.curie('force'),
                   model_uri=CONTAINERS.PodmanSecret_force, domain=PodmanSecret, range=Optional[Union[bool, Bool]])

slots.PodmanSecret_name = Slot(uri=RDFS.label, name="PodmanSecret_name", curie=RDFS.curie('label'),
                   model_uri=CONTAINERS.PodmanSecret_name, domain=PodmanSecret, range=Union[str, LabelType])

slots.PodmanSecret_skip_existing = Slot(uri=CONTAINERS.skip_existing, name="PodmanSecret_skip_existing", curie=CONTAINERS.curie('skip_existing'),
                   model_uri=CONTAINERS.PodmanSecret_skip_existing, domain=PodmanSecret, range=Optional[Union[bool, Bool]])

slots.PodmanSecret_state = Slot(uri=UCO-OBSERVABLE.state, name="PodmanSecret_state", curie=UCO-OBSERVABLE.curie('state'),
                   model_uri=CONTAINERS.PodmanSecret_state, domain=PodmanSecret, range=Optional[str])

slots.PodmanTag_executable = Slot(uri=CORE.executable, name="PodmanTag_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanTag_executable, domain=PodmanTag, range=Optional[str])

slots.PodmanTag_image = Slot(uri=CORE.image, name="PodmanTag_image", curie=CORE.curie('image'),
                   model_uri=CONTAINERS.PodmanTag_image, domain=PodmanTag, range=str)

slots.PodmanTag_target_names = Slot(uri=CONTAINERS.target_names, name="PodmanTag_target_names", curie=CONTAINERS.curie('target_names'),
                   model_uri=CONTAINERS.PodmanTag_target_names, domain=PodmanTag, range=Union[str, List[str]])

slots.PodmanVolume_debug = Slot(uri=CORE.debug, name="PodmanVolume_debug", curie=CORE.curie('debug'),
                   model_uri=CONTAINERS.PodmanVolume_debug, domain=PodmanVolume, range=Optional[Union[bool, Bool]])

slots.PodmanVolume_driver = Slot(uri=CORE.driver, name="PodmanVolume_driver", curie=CORE.curie('driver'),
                   model_uri=CONTAINERS.PodmanVolume_driver, domain=PodmanVolume, range=Optional[str])

slots.PodmanVolume_executable = Slot(uri=CORE.executable, name="PodmanVolume_executable", curie=CORE.curie('executable'),
                   model_uri=CONTAINERS.PodmanVolume_executable, domain=PodmanVolume, range=Optional[str])

slots.PodmanVolume_label = Slot(uri=CORE.label, name="PodmanVolume_label", curie=CORE.curie('label'),
                   model_uri=CONTAINERS.PodmanVolume_label, domain=PodmanVolume, range=Optional[Union[dict, "MetaObject"]])

slots.PodmanVolume_name = Slot(uri=RDFS.label, name="PodmanVolume_name", curie=RDFS.curie('label'),
                   model_uri=CONTAINERS.PodmanVolume_name, domain=PodmanVolume, range=Union[str, LabelType])

slots.PodmanVolume_options = Slot(uri=CORE.options, name="PodmanVolume_options", curie=CORE.curie('options'),
                   model_uri=CONTAINERS.PodmanVolume_options, domain=PodmanVolume, range=Optional[Union[str, List[str]]])

slots.PodmanVolume_recreate = Slot(uri=CORE.recreate, name="PodmanVolume_recreate", curie=CORE.curie('recreate'),
                   model_uri=CONTAINERS.PodmanVolume_recreate, domain=PodmanVolume, range=Optional[Union[bool, Bool]])

slots.PodmanVolume_state = Slot(uri=UCO-OBSERVABLE.state, name="PodmanVolume_state", curie=UCO-OBSERVABLE.curie('state'),
                   model_uri=CONTAINERS.PodmanVolume_state, domain=PodmanVolume, range=Optional[str])

slots.Attribute_name = Slot(uri=RDFS.label, name="Attribute_name", curie=RDFS.curie('label'),
                   model_uri=CONTAINERS.Attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.NamedThing_category = Slot(uri=CORE.category, name="NamedThing_category", curie=CORE.curie('category'),
                   model_uri=CONTAINERS.NamedThing_category, domain=NamedThing, range=Union[Union[str, CategoryType], List[Union[str, CategoryType]]],
                   pattern=re.compile(r'^ucs-core:[A-Z][A-Za-z]+$'))

slots.Association_type = Slot(uri=RDF.type, name="Association_type", curie=RDF.curie('type'),
                   model_uri=CONTAINERS.Association_type, domain=Association, range=Optional[str])

slots.Association_category = Slot(uri=CORE.category, name="Association_category", curie=CORE.curie('category'),
                   model_uri=CONTAINERS.Association_category, domain=Association, range=Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]])