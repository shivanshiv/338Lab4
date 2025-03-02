# Exercise 5

**Question 1**

When timing a program, various factors can introduce measurement noise, such as background processes, CPU load, and system state variations. These factors can lead to fluctuations in execution times, making a single measurement unreliable. The timeit.timeit() function runs the function multiple times (e.g., 100 iterations) and returns the total elapsed time. By executing the function repeatedly within a single call, it mitigates the impact of transient variations but does not provide insight into variability across runs. On the other hand, timeit.repeat() performs multiple independent runs (e.g., 5 times), each executing the function a set number of times (e.g., 10 iterations), returning a list of timings. This method accounts for fluctuations across different runs and helps assess consistency. timeit.timeit() is best used when a single, high-precision measurement is sufficient and when execution time is relatively stable, whereas timeit.repeat() is more useful when analyzing variability across different system conditions or comparing different implementations.


**Question 2**

For timeit.timeit(), since it provides a single measurement representing the total execution time of multiple iterations, the average (total time divided by the number of executions) is the most appropriate statistic. This helps in estimating the time per execution while reducing the impact of outliers. For timeit.repeat(), since it returns multiple values (one per repeat), it allows for deeper statistical analysis. The minimum is often the most appropriate statistic because it represents the best possible performance in ideal conditions, minimizing the impact of external noise. However, analyzing both the minimum and maximum can help understand performance variation. Thus, timeit.timeit() is best analyzed with the average, while timeit.repeat() is best analyzed with the minimum to filter out noise and get an accurate estimate of performance.


