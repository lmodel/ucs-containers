package None;

import java.util.List;
import lombok.*;






/**
  Podman container
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanContainer extends ClosedSoftwareModule {

  private String executable;
  private String state;
  private MetaObject annotation;
  private String authfile;
  private Integer blkioWeight;
  private List<MetaObject> blkioWeightDevice;
  private List<String> capAdd;
  private List<String> capDrop;
  private String cgroupParent;
  private String cgroupns;
  private String cgroups;
  private String cidfile;
  private List<String> cmdArgs;
  private String conmonPidfile;
  private List<String> command;
  private Integer cpuPeriod;
  private Integer cpuRtPeriod;
  private Integer cpuRtRuntime;
  private Integer cpuShares;
  private String cpus;
  private String cpusetCpus;
  private String cpusetMems;
  private boolean detach;
  private boolean debug;
  private String detachKeys;
  private List<String> device;
  private List<String> deviceReadBps;
  private List<String> deviceReadIops;
  private List<String> deviceWriteBps;
  private List<String> deviceWriteIops;
  private List<String> dns;
  private String dnsOption;
  private String dnsSearch;
  private String entrypoint;
  private MetaObject env;
  private String envFile;
  private boolean envHost;
  private MetaObject etcHosts;
  private List<String> expose;
  private boolean forceRestart;
  private MetaObject generateSystemd;
  private List<String> gidmap;
  private List<String> groupAdd;
  private String healthcheck;
  private String healthcheckInterval;
  private Integer healthcheckRetries;
  private String healthcheckStartPeriod;
  private String healthcheckTimeout;
  private String hostname;
  private boolean httpProxy;
  private String imageVolume;
  private boolean imageStrict;
  private boolean init;
  private String initPath;
  private boolean interactive;
  private String ip;
  private String ipc;
  private String kernelMemory;
  private MetaObject label;
  private String labelFile;
  private String logDriver;
  private String logLevel;
  private MetaObject logOpt;
  private String macAddress;
  private String memory;
  private String memoryReservation;
  private String memorySwap;
  private Integer memorySwappiness;
  private List<String> mount;
  private String name;
  private List<String> network;
  private List<String> networkAliases;
  private boolean noHosts;
  private boolean oomKillDisable;
  private Integer oomScoreAdj;
  private String pid;
  private Integer pidsLimit;
  private String pod;
  private boolean privileged;
  private List<String> publish;
  private boolean publishAll;
  private boolean readOnly;
  private boolean readOnlyTmpfs;
  private boolean recreate;
  private List<String> requires;
  private String restartPolicy;
  private boolean rm;
  private boolean rootfs;
  private String sdnotify;
  private List<String> secrets;
  private List<String> securityOpt;
  private String shmSize;
  private boolean sigProxy;
  private Integer stopSignal;
  private Integer stopTimeout;
  private String subgidname;
  private String subuidname;
  private MetaObject sysctl;
  private String systemd;
  private String timezone;
  private MetaObject tmpfs;
  private boolean tty;
  private List<String> uidmap;
  private List<String> ulimit;
  private String user;
  private String userns;
  private String uts;
  private List<String> volume;
  private List<String> volumesFrom;
  private String workdir;

}