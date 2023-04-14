package None;

import java.util.List;
import lombok.*;






/**
  Generate systemd unit from a pod or a container
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PodmanGenerateSystemd extends ClosedSoftwareModule {

  private List<String> after;
  private String containerPrefix;
  private String dest;
  private MetaObject env;
  private String executable;
  private String name;
  private boolean new;
  private boolean noHeader;
  private String podPrefix;
  private List<String> requires;
  private String restartPolicy;
  private Integer restartSec;
  private String separator;
  private Integer startTimeout;
  private Integer stopTimeout;
  private boolean useNames;
  private List<String> wants;

}