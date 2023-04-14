

CREATE TABLE "Agent" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	address TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Container" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Containerd" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Docker" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Hardware" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Kubernetes" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Linux" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Lxc" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "LxcFs" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Lxd" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "OperatingSystem" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PodmanContainer" (
	state VARCHAR(7), 
	annotation TEXT, 
	authfile TEXT, 
	blkio_weight INTEGER, 
	blkio_weight_device TEXT, 
	cap_add TEXT, 
	cap_drop TEXT, 
	cgroup_parent TEXT, 
	cgroupns TEXT, 
	cgroups TEXT, 
	cidfile TEXT, 
	cmd_args TEXT, 
	conmon_pidfile TEXT, 
	command TEXT, 
	cpu_period INTEGER, 
	cpu_rt_period INTEGER, 
	cpu_rt_runtime INTEGER, 
	cpu_shares INTEGER, 
	cpus TEXT, 
	cpuset_cpus TEXT, 
	cpuset_mems TEXT, 
	"detach" BOOLEAN, 
	debug BOOLEAN, 
	detach_keys TEXT, 
	device TEXT, 
	device_read_bps TEXT, 
	device_read_iops TEXT, 
	device_write_bps TEXT, 
	device_write_iops TEXT, 
	dns TEXT, 
	dns_option TEXT, 
	dns_search TEXT, 
	entrypoint TEXT, 
	env TEXT, 
	env_file TEXT, 
	env_host BOOLEAN, 
	etc_hosts TEXT, 
	expose TEXT, 
	force_restart BOOLEAN, 
	generate_systemd TEXT, 
	gidmap TEXT, 
	group_add TEXT, 
	healthcheck TEXT, 
	healthcheck_interval TEXT, 
	healthcheck_retries INTEGER, 
	healthcheck_start_period TEXT, 
	healthcheck_timeout TEXT, 
	hostname TEXT, 
	http_proxy BOOLEAN, 
	image_volume VARCHAR(6), 
	image_strict BOOLEAN, 
	init BOOLEAN, 
	init_path TEXT, 
	interactive BOOLEAN, 
	ip TEXT, 
	ipc TEXT, 
	kernel_memory TEXT, 
	label TEXT, 
	label_file TEXT, 
	log_driver VARCHAR(9), 
	log_level VARCHAR(5), 
	log_opt TEXT, 
	mac_address TEXT, 
	memory TEXT, 
	memory_reservation TEXT, 
	memory_swap TEXT, 
	memory_swappiness INTEGER, 
	mount TEXT, 
	name TEXT NOT NULL, 
	network TEXT, 
	network_aliases TEXT, 
	no_hosts BOOLEAN, 
	oom_kill_disable BOOLEAN, 
	oom_score_adj INTEGER, 
	pid TEXT, 
	pids_limit INTEGER, 
	pod TEXT, 
	privileged BOOLEAN, 
	publish TEXT, 
	publish_all BOOLEAN, 
	read_only BOOLEAN, 
	read_only_tmpfs BOOLEAN, 
	recreate BOOLEAN, 
	requires TEXT, 
	restart_policy TEXT, 
	rm BOOLEAN, 
	rootfs BOOLEAN, 
	sdnotify TEXT, 
	secrets TEXT, 
	security_opt TEXT, 
	shm_size TEXT, 
	sig_proxy BOOLEAN, 
	stop_signal INTEGER, 
	stop_timeout INTEGER, 
	subgidname TEXT, 
	subuidname TEXT, 
	sysctl TEXT, 
	systemd TEXT, 
	timezone TEXT, 
	tmpfs TEXT, 
	tty BOOLEAN, 
	uidmap TEXT, 
	ulimit TEXT, 
	user TEXT, 
	userns TEXT, 
	uts TEXT, 
	volume TEXT, 
	volumes_from TEXT, 
	workdir TEXT, 
	executable TEXT, 
	image TEXT, 
	PRIMARY KEY (state, annotation, authfile, blkio_weight, blkio_weight_device, cap_add, cap_drop, cgroup_parent, cgroupns, cgroups, cidfile, cmd_args, conmon_pidfile, command, cpu_period, cpu_rt_period, cpu_rt_runtime, cpu_shares, cpus, cpuset_cpus, cpuset_mems, "detach", debug, detach_keys, device, device_read_bps, device_read_iops, device_write_bps, device_write_iops, dns, dns_option, dns_search, entrypoint, env, env_file, env_host, etc_hosts, expose, force_restart, generate_systemd, gidmap, group_add, healthcheck, healthcheck_interval, healthcheck_retries, healthcheck_start_period, healthcheck_timeout, hostname, http_proxy, image_volume, image_strict, init, init_path, interactive, ip, ipc, kernel_memory, label, label_file, log_driver, log_level, log_opt, mac_address, memory, memory_reservation, memory_swap, memory_swappiness, mount, name, network, network_aliases, no_hosts, oom_kill_disable, oom_score_adj, pid, pids_limit, pod, privileged, publish, publish_all, read_only, read_only_tmpfs, recreate, requires, restart_policy, rm, rootfs, sdnotify, secrets, security_opt, shm_size, sig_proxy, stop_signal, stop_timeout, subgidname, subuidname, sysctl, systemd, timezone, tmpfs, tty, uidmap, ulimit, user, userns, uts, volume, volumes_from, workdir, executable, image)
);

CREATE TABLE "PodmanContainers" (
	executable TEXT, 
	containers TEXT NOT NULL, 
	debug BOOLEAN, 
	PRIMARY KEY (executable, containers, debug)
);

CREATE TABLE "PodmanExport" (
	container TEXT NOT NULL, 
	dest TEXT NOT NULL, 
	force BOOLEAN, 
	executable TEXT, 
	PRIMARY KEY (container, dest, force, executable)
);

CREATE TABLE "PodmanGenerateSystemd" (
	"after" TEXT, 
	container_prefix TEXT, 
	dest TEXT, 
	env TEXT, 
	name TEXT NOT NULL, 
	new BOOLEAN, 
	no_header BOOLEAN, 
	pod_prefix TEXT, 
	requires TEXT, 
	restart_policy VARCHAR(11), 
	restart_sec INTEGER, 
	separator TEXT, 
	start_timeout INTEGER, 
	stop_timeout INTEGER, 
	use_names BOOLEAN, 
	wants TEXT, 
	executable TEXT, 
	PRIMARY KEY ("after", container_prefix, dest, env, name, new, no_header, pod_prefix, requires, restart_policy, restart_sec, separator, start_timeout, stop_timeout, use_names, wants, executable)
);

CREATE TABLE "PodmanImage" (
	auth_file TEXT, 
	build TEXT, 
	ca_cert_dir TEXT, 
	force BOOLEAN, 
	name TEXT NOT NULL, 
	password TEXT, 
	path TEXT, 
	pull BOOLEAN, 
	push BOOLEAN, 
	push_args TEXT, 
	compress TEXT, 
	dest TEXT, 
	format TEXT, 
	remove_signatures TEXT, 
	sign_by TEXT, 
	transport TEXT, 
	state VARCHAR(7), 
	tag TEXT, 
	username TEXT, 
	validate_certs BOOLEAN, 
	executable TEXT, 
	PRIMARY KEY (auth_file, build, ca_cert_dir, force, name, password, path, pull, push, push_args, compress, dest, format, remove_signatures, sign_by, transport, state, tag, username, validate_certs, executable)
);

CREATE TABLE "PodmanImport" (
	change TEXT, 
	commit_message TEXT, 
	src TEXT NOT NULL, 
	executable TEXT, 
	PRIMARY KEY (change, commit_message, src, executable)
);

CREATE TABLE "PodmanLoad" (
	input TEXT NOT NULL, 
	executable TEXT, 
	PRIMARY KEY (input, executable)
);

CREATE TABLE "PodmanLogin" (
	authfile TEXT, 
	certdir TEXT, 
	password TEXT NOT NULL, 
	registry TEXT, 
	tlsverify BOOLEAN, 
	username TEXT NOT NULL, 
	executable TEXT, 
	PRIMARY KEY (authfile, certdir, password, registry, tlsverify, username, executable)
);

CREATE TABLE "PodmanLogout" (
	"all" BOOLEAN, 
	authfile TEXT, 
	ignore_docker_credentials BOOLEAN, 
	executable TEXT, 
	registry TEXT, 
	PRIMARY KEY ("all", authfile, ignore_docker_credentials, executable, registry)
);

CREATE TABLE "PodmanNetwork" (
	debug BOOLEAN, 
	disable_dns BOOLEAN, 
	driver TEXT, 
	gateway TEXT, 
	internal BOOLEAN, 
	ip_range TEXT, 
	ipv6 BOOLEAN, 
	macvlan TEXT, 
	name TEXT NOT NULL, 
	opt TEXT, 
	recreate BOOLEAN, 
	state VARCHAR(7), 
	subnet TEXT, 
	executable TEXT, 
	PRIMARY KEY (debug, disable_dns, driver, gateway, internal, ip_range, ipv6, macvlan, name, opt, recreate, state, subnet, executable)
);

CREATE TABLE "PodmanPlay" (
	authfile TEXT, 
	cert_dir TEXT, 
	configmap TEXT, 
	debug BOOLEAN, 
	kube_file TEXT NOT NULL, 
	log_driver TEXT, 
	log_level VARCHAR(5), 
	network TEXT, 
	password TEXT, 
	quiet BOOLEAN, 
	recreate BOOLEAN, 
	seccomp_profile_root TEXT, 
	state VARCHAR(7) NOT NULL, 
	tls_verify BOOLEAN, 
	username TEXT, 
	executable TEXT, 
	PRIMARY KEY (authfile, cert_dir, configmap, debug, kube_file, log_driver, log_level, network, password, quiet, recreate, seccomp_profile_root, state, tls_verify, username, executable)
);

CREATE TABLE "PodmanPod" (
	add_host TEXT, 
	cgroup_parent TEXT, 
	cpus TEXT, 
	cpuset_cpus TEXT, 
	debug BOOLEAN, 
	device TEXT, 
	device_read_bps TEXT, 
	dns TEXT, 
	dns_opt TEXT, 
	dns_search TEXT, 
	generate_systemd TEXT, 
	gidmap TEXT, 
	hostname TEXT, 
	infra BOOLEAN, 
	infra_command TEXT, 
	infra_conmon_pidfile TEXT, 
	infra_name TEXT, 
	infra_image TEXT, 
	ip TEXT, 
	label TEXT, 
	label_file TEXT, 
	mac_address TEXT, 
	name TEXT NOT NULL, 
	network TEXT, 
	network_alias TEXT, 
	no_hosts BOOLEAN, 
	pid TEXT, 
	pod_id_file TEXT, 
	publish TEXT, 
	recreate BOOLEAN, 
	share TEXT, 
	state VARCHAR(7), 
	subgidname TEXT, 
	subuidname TEXT, 
	uidmap TEXT, 
	userns TEXT, 
	volume TEXT, 
	executable TEXT, 
	PRIMARY KEY (add_host, cgroup_parent, cpus, cpuset_cpus, debug, device, device_read_bps, dns, dns_opt, dns_search, generate_systemd, gidmap, hostname, infra, infra_command, infra_conmon_pidfile, infra_name, infra_image, ip, label, label_file, mac_address, name, network, network_alias, no_hosts, pid, pod_id_file, publish, recreate, share, state, subgidname, subuidname, uidmap, userns, volume, executable)
);

CREATE TABLE "PodmanSave" (
	compress BOOLEAN, 
	dest TEXT NOT NULL, 
	force BOOLEAN, 
	format VARCHAR(14), 
	image TEXT NOT NULL, 
	multi_image_archive BOOLEAN, 
	executable TEXT, 
	PRIMARY KEY (compress, dest, force, format, image, multi_image_archive, executable)
);

CREATE TABLE "PodmanSecret" (
	data TEXT, 
	driver TEXT, 
	driver_opts TEXT, 
	force BOOLEAN, 
	name TEXT NOT NULL, 
	skip_existing BOOLEAN, 
	state TEXT, 
	executable TEXT, 
	PRIMARY KEY (data, driver, driver_opts, force, name, skip_existing, state, executable)
);

CREATE TABLE "PodmanTag" (
	image TEXT NOT NULL, 
	target_names TEXT NOT NULL, 
	executable TEXT, 
	PRIMARY KEY (image, target_names, executable)
);

CREATE TABLE "PodmanVolume" (
	debug BOOLEAN, 
	driver TEXT, 
	label TEXT, 
	name TEXT NOT NULL, 
	options TEXT, 
	recreate BOOLEAN, 
	state TEXT, 
	executable TEXT, 
	PRIMARY KEY (debug, driver, label, name, options, recreate, state, executable)
);

CREATE TABLE "Project" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "QuantityValue" (
	"hasUnit" TEXT, 
	"hasNumericValue" FLOAT, 
	PRIMARY KEY ("hasUnit", "hasNumericValue")
);

CREATE TABLE "Software" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Solaris" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "System" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Windows" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Association" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "NamedThing" (id), 
	FOREIGN KEY(object) REFERENCES "NamedThing" (id)
);

CREATE TABLE "Attribute" (
	name TEXT, 
	"hasAttributeType" TEXT NOT NULL, 
	"hasQuantitativeValue" TEXT, 
	"hasQualitativeValue" TEXT, 
	iri TEXT, 
	src TEXT, 
	PRIMARY KEY (name, "hasAttributeType", "hasQuantitativeValue", "hasQualitativeValue", iri, src), 
	FOREIGN KEY("hasQualitativeValue") REFERENCES "NamedThing" (id)
);

CREATE TABLE "Agent_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Agent_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Agent_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Agent_affiliation" (
	backref_id TEXT, 
	affiliation TEXT, 
	PRIMARY KEY (backref_id, affiliation), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Container_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Container" (id)
);

CREATE TABLE "Container_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Container" (id)
);

CREATE TABLE "Container_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Container" (id)
);

CREATE TABLE "Containerd_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Containerd" (id)
);

CREATE TABLE "Containerd_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Containerd" (id)
);

CREATE TABLE "Containerd_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Containerd" (id)
);

CREATE TABLE "Docker_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Docker" (id)
);

CREATE TABLE "Docker_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Docker" (id)
);

CREATE TABLE "Docker_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Docker" (id)
);

CREATE TABLE "Hardware_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Hardware" (id)
);

CREATE TABLE "Hardware_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Hardware" (id)
);

CREATE TABLE "Hardware_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Hardware" (id)
);

CREATE TABLE "Kubernetes_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Kubernetes" (id)
);

CREATE TABLE "Kubernetes_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Kubernetes" (id)
);

CREATE TABLE "Kubernetes_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Kubernetes" (id)
);

CREATE TABLE "Linux_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Linux" (id)
);

CREATE TABLE "Linux_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Linux" (id)
);

CREATE TABLE "Linux_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Linux" (id)
);

CREATE TABLE "Lxc_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Lxc" (id)
);

CREATE TABLE "Lxc_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Lxc" (id)
);

CREATE TABLE "Lxc_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Lxc" (id)
);

CREATE TABLE "LxcFs_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "LxcFs" (id)
);

CREATE TABLE "LxcFs_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "LxcFs" (id)
);

CREATE TABLE "LxcFs_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "LxcFs" (id)
);

CREATE TABLE "Lxd_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Lxd" (id)
);

CREATE TABLE "Lxd_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Lxd" (id)
);

CREATE TABLE "Lxd_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Lxd" (id)
);

CREATE TABLE "NamedThing_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "NamedThing" (id)
);

CREATE TABLE "NamedThing_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "NamedThing" (id)
);

CREATE TABLE "NamedThing_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "NamedThing" (id)
);

CREATE TABLE "OperatingSystem_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "OperatingSystem" (id)
);

CREATE TABLE "OperatingSystem_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "OperatingSystem" (id)
);

CREATE TABLE "OperatingSystem_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "OperatingSystem" (id)
);

CREATE TABLE "Project_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Project" (id)
);

CREATE TABLE "Project_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Project" (id)
);

CREATE TABLE "Project_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Project" (id)
);

CREATE TABLE "Software_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);

CREATE TABLE "Software_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);

CREATE TABLE "Software_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);

CREATE TABLE "Solaris_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Solaris" (id)
);

CREATE TABLE "Solaris_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Solaris" (id)
);

CREATE TABLE "Solaris_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Solaris" (id)
);

CREATE TABLE "System_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "System" (id)
);

CREATE TABLE "System_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "System" (id)
);

CREATE TABLE "System_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "System" (id)
);

CREATE TABLE "Windows_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Windows" (id)
);

CREATE TABLE "Windows_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Windows" (id)
);

CREATE TABLE "Windows_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Windows" (id)
);

CREATE TABLE "EvidenceType" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	"creationDate" DATE, 
	"Association_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Association_id") REFERENCES "Association" (id)
);

CREATE TABLE "Publication" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	"creationDate" DATE, 
	summary TEXT, 
	"Association_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Association_id") REFERENCES "Association" (id)
);

CREATE TABLE "Association_qualifiers" (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Association" (id)
);

CREATE TABLE "Association_category" (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Association" (id)
);

CREATE TABLE "EvidenceType_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "EvidenceType" (id)
);

CREATE TABLE "EvidenceType_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "EvidenceType" (id)
);

CREATE TABLE "EvidenceType_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "EvidenceType" (id)
);

CREATE TABLE "Publication_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_authors" (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_pages" (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_lcshTerms" (
	backref_id TEXT, 
	"lcshTerms" TEXT, 
	PRIMARY KEY (backref_id, "lcshTerms"), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);
