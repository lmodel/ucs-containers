package None;

import java.util.List;
import lombok.*;






/**
  Add an additional name to a local image
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanTag extends ClosedSoftwareModule {

  private String executable;
  private String image;
  private List<String> targetNames;

}