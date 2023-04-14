package None;

import java.util.List;
import lombok.*;






/**
  Logout of a Container registry using Podman
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanLogout extends ClosedSoftwareModule {

  private boolean all;
  private String authfile;
  private String executable;
  private boolean ignoreDockerCredentials;

}