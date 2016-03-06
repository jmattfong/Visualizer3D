/**
 * Resources.java
 *
 * This file is subject to the terms and conditions defined in
 * file 'LICENSE', which is part of this source code package.
 *
 * Copyright (C) 2016, Matthew Fong
 */
package com.visualizer.res;

import java.awt.Image;
import java.io.IOException;
import java.io.UncheckedIOException;

import javax.imageio.ImageIO;

public class Resources {

	public static Image getImage(Resource res) {
		Image img = null;
		try {
			System.out.println("img: " + img);
			img = ImageIO.read(Resources.class.getResource(res.getPath()));
			System.out.println("img2: " + img);
		} catch (IOException e) {
			System.out.println("caught exception: " + e);
			throw new UncheckedIOException(e);
		}
		return img;
	}

}
