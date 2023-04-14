package None;

import java.util.List;
import lombok.*;






/**
  Saves podman image to tar file
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanSave extends ClosedSoftwareModule {

  private boolean compress;
  private String dest;
  private boolean force;
  private String format;
  private String image;
  private boolean multiImageArchive;

}