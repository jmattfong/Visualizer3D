/**
 * ImagePanel.java
 *
 * This file is subject to the terms and conditions defined in
 * file 'LICENSE', which is part of this source code package.
 *
 * Copyright (C) 2016, Matthew Fong
 */
package com.visualizer.ui;

import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Image;

import javax.swing.JPanel;

import com.visualizer.res.R;
import com.visualizer.res.Resources;

public class ImagePanel extends JPanel {

	private static final int PREFERRED_WIDTH = 1000;
	private static final int PREFERRED_HEIGHT = 500;

	private static final long serialVersionUID = 1L;

	private Image mImage;

	public ImagePanel() {
		mImage = Resources.getImage(R.images.values()[0]);
		setPreferredSize(new Dimension(PREFERRED_WIDTH, PREFERRED_HEIGHT));
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		g.drawImage(mImage, 0, 0, null);
	}

}