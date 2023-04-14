package None;

import java.util.List;
import lombok.*;






/**
  Podman containers
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanContainers extends ClosedSoftwareModule {

  private List<MetaObject> containers;
  private boolean debug;

}