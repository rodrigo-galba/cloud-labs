# How to calculate the SLA of multiple components

To calculate the SLA of multiple components, you can use the formula for availability, which is the percentage of time that the service is available and functioning correctly.

> The formula is: Availabity = (Uptime / (Uptime + Downtime)) x 100.

To use this formula, you need to multiply the availability of each component together, and then take the resulting value to the power of the number of components.

For example, if you have a load balancer with a SLA of 99.95%, a website with a SLA of 99.95%, and a database with a SLA of 99.99%, you can calculate the overwall SLA as:

> Overall SLA = 0.9995 * 0.9995 * 0.9999 = 0.9989, or 99.89%

Keep in mind that this method assumes that the individual components are independent and failure of one component does not affect the others, which is not always the case.  

What if we deploy to another region as well and want to get a parallel composite SLA.

The unavailability for each region is 100-99.89 = 0.11  
Which makes the multi region unavailability: (R1 * R2)/100 = (0.11 * 0.11)/100 = 0.000121  

> Making the SLA: 100-0.0121 = 99.999879

You do need a load balancer for the regions, assume it has a SLA of 99.99%.  
Your total SLA will be 99.99 * 99.999879 = 99.9897%

This is around 53 minutes a year: (https://uptime.is/99.9897)