/**
 * Visualizer.java
 *
 * This file is subject to the terms and conditions defined in
 * file 'LICENSE', which is part of this source code package.
 *
 * Copyright (C) 2016, Matthew Fong
 */
package com.visualizer.ui;

import javax.swing.JFrame;

public class Visualizer {

	private final ImagePanel mImagePanel;

	public Visualizer(String[] args) {
		mImagePanel = new ImagePanel();
	}

	/**
	 * Create the GUI and show it. For thread safety, this method should be
	 * invoked from the event-dispatching thread.
	 */
	public void createAndShowGUI() {
		// Create and set up the window.
		JFrame frame = new JFrame("HelloWorldSwing");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		frame.getContentPane().add(mImagePanel);

		// Display the window.
		frame.pack();
		frame.setVisible(true);
	}

}
