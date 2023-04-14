package None;

import java.util.List;
import lombok.*;






/**
  Podman container image
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanImage extends ClosedSoftwareModule {

  private String authFile;
  private MetaObject build;
  private String caCertDir;
  private String executable;
  private boolean force;
  private String name;
  private String password;
  private String path;
  private boolean pull;
  private boolean push;
  private MetaObject pushArgs;
  private String compress;
  private String dest;
  private String format;
  private String removeSignatures;
  private String signBy;
  private String transport;
  private String state;
  private String tag;
  private String username;
  private boolean validateCerts;

}