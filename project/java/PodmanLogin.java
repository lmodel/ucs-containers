package None;

import java.util.List;
import lombok.*;






/**
  Login to a Container registry using Podman
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanLogin extends ClosedSoftwareModule {

  private String authfile;
  private String certdir;
  private String executable;
  private String password;
  private String registry;
  private boolean tlsverify;
  private String username;

}