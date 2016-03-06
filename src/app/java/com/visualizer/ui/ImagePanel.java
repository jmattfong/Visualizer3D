/**
 * ImagePanel.java
 *
 * This file is subject to the terms and conditions defined in
 * file 'LICENSE', which is part of this source code package.
 *
 * Copyright (C) 2016, Matthew Fong
 */
package com.visualizer.ui;

import java.awt.Graphics;
import java.awt.Image;

import javax.swing.JPanel;

import com.visualizer.res.Resource;
import com.visualizer.res.Resources;

public class ImagePanel extends JPanel {

	private static final long serialVersionUID = 1L;

	private Image mImage;

	public ImagePanel(Resource res) {
		mImage = Resources.getImage(res);
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		g.drawImage(mImage, 0, 0, null);
	}

}