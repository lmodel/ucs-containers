package None;

import java.util.List;
import lombok.*;






/**
  Import Podman container from file
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanImport extends ClosedSoftwareModule {

  private List<MetaObject> change;
  private String commitMessage;
  private String src;

}