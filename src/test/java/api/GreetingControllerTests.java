package api;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

import java.util.concurrent.TimeUnit;

public class GreetingControllerTests {

	@Test
	public void test1() {

		Assert.assertTrue(true);
	}

	@Test
	public void test2() {

		Assert.assertTrue(true);
	}

	@Test
	public void test3() {
		try {
			TimeUnit.SECONDS.sleep(3);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		Assert.assertTrue(true);
	}
}