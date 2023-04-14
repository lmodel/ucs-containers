package None;

import java.util.List;
import lombok.*;






/**
  Manage podman networks
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanNetwork extends ClosedSoftwareModule {

  private boolean debug;
  private boolean disableDns;
  private String driver;
  private String executable;
  private String gateway;
  private boolean internal;
  private String ipRange;
  private boolean ipv6;
  private String macvlan;
  private String name;
  private MetaObject opt;
  private boolean recreate;
  private String state;
  private String subnet;

}