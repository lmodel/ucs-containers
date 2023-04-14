package None;

import java.util.List;
import lombok.*;






/**
  Manage Podman secrets
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanSecret extends ClosedSoftwareModule {

  private String data;
  private String driver;
  private MetaObject driverOpts;
  private String executable;
  private boolean force;
  private String name;
  private boolean skipExisting;
  private String state;

}