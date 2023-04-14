package None;

import java.util.List;
import lombok.*;






/**
  Manage Podman pods
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanPod extends ClosedSoftwareModule {

  private List<String> addHost;
  private String cgroupParent;
  private String cpus;
  private String cpusetCpus;
  private boolean debug;
  private List<String> device;
  private List<String> deviceReadBps;
  private List<String> dns;
  private List<String> dnsOpt;
  private List<String> dnsSearch;
  private String executable;
  private MetaObject generateSystemd;
  private List<String> gidmap;
  private String hostname;
  private boolean infra;
  private String infraCommand;
  private String infraConmonPidfile;
  private String infraName;
  private String infraImage;
  private String ip;
  private MetaObject label;
  private String labelFile;
  private String macAddress;
  private String name;
  private List<String> network;
  private List<String> networkAlias;
  private boolean noHosts;
  private String pid;
  private String podIdFile;
  private List<String> publish;
  private boolean recreate;
  private String share;
  private String state;
  private String subgidname;
  private String subuidname;
  private List<String> uidmap;
  private String userns;
  private List<String> volume;

}