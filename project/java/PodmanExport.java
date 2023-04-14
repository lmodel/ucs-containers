package None;

import java.util.List;
import lombok.*;






/**
  Export a Podman container
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanExport extends ClosedSoftwareModule {

  private String container;
  private String dest;
  private String executable;
  private boolean force;

}