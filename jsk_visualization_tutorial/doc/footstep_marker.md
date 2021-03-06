# jsk_interactive_marker/footstep_marker

[document for jsk_footstep_planner](http://jsk-docs.readthedocs.io/en/latest/jsk_control/doc/jsk_footstep_planner/README.html)

## parameters for robot
### jaxon.yaml
```
# jaxon.yaml
footstep_margin: 0.2
# coordinate system
lfoot_frame_id: LLEG_LINK5
rfoot_frame_id: RLEG_LINK5
# offset link coordinate -> center of foot
lfoot_offset: [0.03, 0.01, -0.105, 0, 0, 0, 1]
rfoot_offset: [0.03, -0.01, -0.105, 0, 0, 0, 1]
# offset link coordinate -> end coords
lfoot_endcoords_offset: [0.035589, 0.01, -0.105, 0, 0, 0, 1]
rfoot_endcoords_offset: [0.035589, -0.01, -0.105, 0, 0, 0, 1]
lleg_vertices: [[-0.100445, -0.055992], [-0.100445, 0.075992], [0.133242, 0.075992], [0.133242, -0.055992]]
rleg_vertices: [[-0.100445, -0.075992], [-0.100445, 0.055992], [0.133242, 0.055992], [0.133242, -0.075992]]
```



```
<rosparam command="load" file="$(find jsk_footstep_controller)/config/$(env ROBOT).yaml" />
<remap from="project_footprint" to="/footstep_planner/project_footprint_with_local_search" />
<remap from="/footstep_controller" to="simple_footstep_controller" if="$(arg USE_SIMPLE_FOOTSTEP_CONTROLLER)"/>
<rosparam subst_value="true">
use_plane_snap: $(arg USE_PERCEPTION)
use_projection_service: true
use_projection_topic: false
use_footstep_planner: true
use_footstep_controller: true
use_initial_footstep_tf: true
use_initial_reference: true
initial_reference_frame: 'ground'
foot_size_x: 0.2
foot_size_y: 0.1
foot_size_z: 0.0001
frame_id: $(arg GLOBAL_FRAME)
</rosparam>
```

