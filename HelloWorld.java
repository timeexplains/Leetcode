import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.lang.management.MemoryUsage;
import java.lang.management.ThreadMXBean;
public class HelloWorld {
	public static void main(String[] args) {
		
		ThreadMXBean threadMXBean = ManagementFactory.getThreadMXBean();
	
		for(int i=0;i<10000000;i++);
		System.out.println("Hello.");
		MemoryMXBean memoryMXBean = ManagementFactory.getMemoryMXBean();
		MemoryUsage memoryUsage = memoryMXBean.getHeapMemoryUsage(); //׵�ڴ�ʹ�����
		long totalMemorySize = memoryUsage.getInit(); //��ʼ�����ڴ�
		long maxMemorySize = memoryUsage.getMax(); //�������ڴ�
		long usedMemorySize = memoryUsage.getUsed(); //��ʹ�õ��ڴ�
		System.out.println(usedMemorySize);
		System.out.println(threadMXBean.getCurrentThreadCpuTime());
	}

}
