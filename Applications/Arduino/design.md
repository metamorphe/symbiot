## TopoTree{Bean} ##
+ .getById()
+ .getByName()
+ .getByGroup()
+ .getNearLocation(pos, distance, limit)


## Bean (view, mcu) ##
+ Actuator
+ MAC address
+ neighbor*   
+ play(Behavior b)


## SpatialBean extends Bean ##
<!-- Grouping class -->
+ Location


## Actuator ##
+
+ ```device_type```
+ dev_category

#### Location ####
+ location_name
+ location_gps (unique coordinate space)


## Symbiot (controller) ##


## Socket ##
+ send()
+ receive()
+ init()


## Behavior(model) ##
+ wave



<!-- GLOBAL -->
## Scheduler ##
+ setTimeout()
+ setInterval()
+ setInvokeLater()


<!-- STATIC !!! -->

/* SpatialUtil */
+ static stream(selector)