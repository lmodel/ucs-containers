package None;

import java.util.List;
import lombok.*;






/**
  Play kubernetes YAML file using podman
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanPlay extends ClosedSoftwareModule {

  private String authfile;
  private String certDir;
  private List<String> configmap;
  private boolean debug;
  private String kubeFile;
  private String logDriver;
  private String logLevel;
  private List<String> network;
  private String password;
  private boolean quiet;
  private boolean recreate;
  private String seccompProfileRoot;
  private String state;
  private boolean tlsVerify;
  private String username;

}