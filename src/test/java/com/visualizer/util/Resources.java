/**
 * Resources.java
 *
 * This file is subject to the terms and conditions defined in
 * file 'LICENSE', which is part of this source code package.
 *
 * Copyright (C) 2016, Matthew Fong
 */
package com.visualizer.util;

import java.awt.Image;
import java.io.IOException;
import java.io.UncheckedIOException;

import javax.imageio.ImageIO;

public class Resources {

	public static Image getImage(String name) {
		Image img = null;
		try {
			img = ImageIO.read(Resources.class.getResource(name));
		} catch (IOException e) {
			throw new UncheckedIOException(e);
		}
		return img;
	}

}
