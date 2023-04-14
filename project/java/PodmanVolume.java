package None;

import java.util.List;
import lombok.*;






/**
  Manage Podman Volumes
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanVolume extends ClosedSoftwareModule {

  private boolean debug;
  private String driver;
  private MetaObject label;
  private String name;
  private List<String> options;
  private boolean recreate;
  private String state;

}