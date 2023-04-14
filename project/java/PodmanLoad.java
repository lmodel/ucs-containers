package None;

import java.util.List;
import lombok.*;






/**
  Load container into container storage
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanLoad extends ClosedSoftwareModule {

  private String input;

}